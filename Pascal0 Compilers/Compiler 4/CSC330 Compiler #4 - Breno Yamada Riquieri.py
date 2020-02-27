#########################################################
#   Name:       Breno Yamada Riquieri                   #
#   Class:      CSC330 - Programming Languages          #
#   A:          Compiler Program #4                     #
#   Due Date:   2/28/2020 - 03/02/2020                  #
#                                                       #
#   Notes:      All 5 test cases compiling successfully #
#               Fibonacci and Hanoi working             #
#########################################################
import sys, string

norw = 28      # updated number of reserved words
txmax = 100   #length of identifier table
nmax = 14      #max number of digits in number
al = 10          #length of identifiers
CXMAX = 500 #maximum allowed lines of assembly code
STACKSIZE = 500
a = []
chars = []
rword = []
table = []         #symbol table
code = []         #code array
stack = [0] * STACKSIZE     #interpreter stack
global infile, outfile, ch, sym, id, num, linlen, kk, line, errorFlag, linelen, codeIndx, prevIndx, codeIndx0
#-------------values to put in the symbol table------------------------------------------------------------
class tableValue():                          
    def __init__(self, name, kind, level, adr, value):
        self.name = name
        self.kind = kind
        self.adr = adr
        self.value = value
        self.level = level
        # ADDED: parameter list of booleans
        if kind == "function" or kind == "procedure":
            self.params = []
#----------commands to put in the array of assembly code-----------------------------------------------
class Cmd():                            
    def __init__(self, line, cmd, statLinks, value):
        self.line = line
        self.cmd = cmd
        self.statLinks = statLinks
        self.value = value
#-------------function to generate assembly commands--------------------------------------------------
def gen(cmd, statLinks, value):            
    global codeIndx, CXMAX
    if codeIndx > CXMAX:
        print >>outfile, "Error, Program is too long"
        exit(0)
    x = Cmd(codeIndx, cmd, statLinks, value)
    code.append(x)
    codeIndx += 1
#--------------function to change jump commands---------------------------------------
def fixJmp(cx, jmpTo):
    code[cx].value = jmpTo
#--------------Function to print p-Code for a given block-----------------------------
def printCode():
    global codeIndx, codeIndx0
    print>>outfile
    for i  in range(codeIndx0, codeIndx):
        print >>outfile, code[i].line, code[i].cmd, code[i].statLinks, code[i].value
    prevIndx = codeIndx
#-------------Function to find a new base----------------------------------------------
def Base(statLinks, base):
    b1 = base
    while(statLinks > 0):
        b1 = stack[b1]
        statLinks -= 1
    return b1
#-------------P-Code Interpreter-------------------------------------------------------
def Interpret():
    print >>outfile, "Start PL/0"
    top = 0
    base = 1
    pos = 0
    stack[1] = 0
    stack[2] = 0
    stack[3] = 0
    while True:
        instr = code[pos]
        pos += 1
        #       LIT COMMAND
        if instr.cmd == "LIT":    
            top += 1
            stack[top] = int(instr.value)
        #       OPR COMMAND
        elif instr.cmd == "OPR":
            if instr.value == 0:         #end
                top = base - 1
                base = stack[top+2]
                pos = stack[top + 3]
            elif instr.value == 1:         #unary minus
                stack[top] = -stack[top]
            elif instr.value == 2:         #addition
                top -= 1
                stack[top] = stack[top] + stack[top+1]
            elif instr.value == 3:         #subtraction
                top -= 1
                stack[top] = stack[top] - stack[top+1]
            elif instr.value == 4:         #multiplication
                top -= 1
                stack[top] = stack[top] * stack[top+1]
            elif instr.value == 5:         #integer division
                top -= 1
                stack[top] = stack[top] / stack[top+1]
            elif instr.value == 6:         #logical odd function
                if stack[top] % 2 == 0:
                    stack[top] = 1
                else:
                    stack[top] = 0
            # case 7 n/a, used to debuge programs
            elif instr.value == 8:        #test for equality if stack[top-1] = stack[top], replace pair with true, otherwise false
                top -= 1
                if stack[top] == stack[top+1]:
                    stack[top] = 1
                else:
                    stack[top] = 0
            elif instr.value == 9:         #test for inequality
                top -= 1
                if stack[top] != stack[top+1]:
                    stack[top] = 1
                else:
                    stack[top] = 0
            elif instr.value == 10:         #test for < (if stack[top-1] < stack[t])
                top -= 1
                if stack[top] < stack[top+1]:
                    stack[top] = 1
                else:
                    stack[top] = 0
            elif instr.value == 11:        #test for >=
                top -= 1
                if stack[top] >= stack[top+1]:
                    stack[top] = 1
                else:
                    stack[top] = 0
            elif instr.value == 12:        #test for >
                top -= 1
                if stack[top] > stack[top+1]:
                    stack[top] = 1
                else:
                    stack[top] = 0
            elif instr.value == 13:        #test for <=
                top -= 1
                if stack[top] <= stack[top+1]:
                    stack[top] = 1
                else:
                    stack[top] = 0
            elif instr.value == 14:        #write/print stack[top]  
                print >>outfile, stack[top],
                top -= 1
            elif instr.value == 15:        #write/print a newline
                print
        #      LOD COMMAND
        elif instr.cmd == "LOD":
            top += 1
            stack[top] = stack[Base(instr.statLinks, base) + instr.value]
        #    STO COMMAND
        elif instr.cmd == "STO":
            stack[Base(instr.statLinks, base) + instr.value] = stack[top]
            top -= 1
        #    CAL COMMAND
        elif instr.cmd == "CAL": 
            stack[top+1] = Base(instr.statLinks, base)
            stack[top+2] = base
            stack[top+3] = pos
            base = top + 1
            pos = instr.value
        #    INT COMMAND
        elif instr.cmd == "INT":
            top = top + instr.value
        #     JMP COMMAND
        elif instr.cmd == "JMP":
            pos = instr.value
        #     JPC COMMAND
        elif instr.cmd == "JPC":
            if stack[top] == instr.statLinks:
                pos = instr.value
            top -= 1
        elif instr.cmd == "CTS":
            top += 1
            stack[top] = stack[top-1]
        ####################### CHANGES STARTING HERE #####################
        elif instr.cmd == "STI":
            stack[stack[Base(instr.statLinks, base) + instr.value]] = stack[top]
            top -= 1
        elif instr.cmd == "LDI":
            top += 1
            stack[top] = stack[stack[Base(instr.statLinks, base) + instr.value]]
        elif instr.cmd == "LDA":
            top += 1
            stack[top] = Base(instr.statLinks, base) + instr.value
        ####################### CHANGES ENDING HERE #####################
        if pos == 0:
            break
    print "End PL/0"
#--------------Error Messages----------------------------------------------------------
def error(num):
    global errorFlag;
    errorFlag = 1
    print
    if num == 1: 
        print >>outfile, "Use = instead of :="
    elif num == 2: 
        print >>outfile, "= must be followed by a number."
    elif num == 3: 
        print >>outfile, "Identifier must be followed by ="
    elif num == 4: 
        print >>outfile, "Const, Var, Procedure must be followed by an identifier."
    elif num == 5: 
        print >>outfile, "Semicolon or comman missing"
    elif num == 6: 
        print >>outfile, "Incorrect symbol after procedure declaration."
    elif num == 7:  
        print >>outfile, "Statement expected."
    elif num == 8:
        print >>outfile, "Incorrect symbol after statment part in block."
    elif num == 9:
        print >>outfile, "Period expected."
    elif num == 10: 
        print >>outfile, "Semicolon between statements is missing."
    elif num == 11:  
        print >>outfile, "Undeclared identifier"
    elif num == 12:
        print >>outfile, "Assignment to a constant or procedure is not allowed."
    elif num == 13:
        print >>outfile, "Assignment operator := expected."
    elif num == 14: 
        print >>outfile, "call must be followed by an identifier"
    elif num == 15:  
        print >>outfile, "Call of a constant or a variable is meaningless."
    elif num == 16:
        print >>outfile, "Then expected"
    elif num == 17:
        print >>outfile, "Semicolon or end expected. "
    elif num == 18: 
        print >>outfile, "DO expected"
    elif num == 19:  
        print >>outfile, "Incorrect symbol following statement"
    elif num == 20:
        print >>outfile, "Relational operator expected."
    elif num == 21:
        print >>outfile, "Expression must not contain a procedure identifier"
    elif num == 22: 
        print >>outfile, "Right parenthesis missing"
    elif num == 23:  
        print >>outfile, "The preceding factor cannot be followed by this symbol."
    elif num == 24:
        print >>outfile, "An expression cannot begin with this symbol."
    elif num == 25:
        print >>outfile, "Constant or Number is expected."
    elif num == 26: 
        print >>outfile, "This number is too large."
    elif num == 27:
        print >>outfile, "UNTIL expected after REPEAT."
    elif num == 28:
        print >>outfile, "TO or DOWNTO expected."
    elif num == 29:
        print >>outfile, "Print statement missing left parenthesis."
    elif num == 30:
        print >>outfile, "OF expected."
    elif num == 31:
        print >>outfile, "Colon expected after number/ident."
    elif num == 32:
        print >>outfile, "Semicolon expected after case statement."
    elif num == 33:
        print >>outfile, "Cend expected."
    elif num == 34:
        print >>outfile, "Const expected"
    elif num == 35:
        print >>outfile, "Must be function."
    elif num == 36:
        print >>outfile, "Expected variable, function, value, or reference."    # added value and reference to the error
    elif num == 37:
        print >>outfile, "Can't assign to this function here."
    ####################### CHANGES STARTING HERE #####################
    elif num == 38:
        print >>outfile, "Expected value or reference."
    ####################### CHANGES ENDING HERE #####################

    exit(0)
#---------GET CHARACTER FUNCTION-------------------------------------------------------------------
def getch():
    global  whichChar, ch, linelen, line;
    if whichChar == linelen:         #if at end of line
        whichChar = 0
        line = infile.readline()     #get next line
        linelen = len(line)
        sys.stdout.write(line)
    if linelen != 0:
        ch = line[whichChar]
        whichChar += 1
    return ch
#----------GET SYMBOL FUNCTION---------------------------------------------------------------------
def getsym():
    global charcnt, ch, al, a, norw, rword, sym, nmax, id, num
    while ch == " " or ch == "\n" or ch == "\r":
        getch()
    a = []
    if ch.isalpha():
        k = 0
        while True:
            a.append(string.upper(ch))
            getch()
            if not ch.isalnum():
                break
        id = "".join(a)
        flag = 0
        for i in range(0, norw):
            if rword[i] == id:
                sym = rword[i]
                flag = 1
        if  flag == 0:    #sym is not a reserved word
            sym = "ident"
    elif ch.isdigit():
        k=0
        num=0
        sym = "number"
        while True:
            a.append(ch)
            k += 1
            getch()
            if not ch.isdigit():
                break
        if k>nmax:
            error(30)
        else:
            num = "".join(a)
    elif ch == ':':
        getch()
        if ch == '=':
            sym = "becomes"
            getch()
        else:
            sym = "colon"
    elif ch == '>':
        getch()
        if ch == '=':
            sym = "geq"
            getch()
        else:
            sym = "gtr"
    elif ch == '<':
        getch()
        if ch == '=':
            sym = "leq"
            getch()
        elif ch == '>':
            sym = "neq"
            getch()
        else:
            sym = "lss"
    else:
        sym = ssym[ch]
        getch()
#--------------POSITION FUNCTION----------------------------
def position(tx, id):
    global  table;
    table[0] = tableValue(id, "TEST", "TEST", "TEST", "TEST")
    i = tx
    while table[i].name != id:
        i=i-1
    return i
#---------------ENTER PROCEDURE-------------------------------
def enter(tx, k, level, dx):
    global id, num, codeIndx;
    tx[0] += 1
    while (len(table) > tx[0]):
      table.pop()
    if k == "const":
        x = tableValue(id, k, level, "NULL", num)
    elif k == "variable":
        x = tableValue(id, k, level, dx, "NULL")
        dx += 1
    elif k == "procedure":
        x = tableValue(id, k, level, dx, "NULL")
    elif k == "function":
        x = tableValue(id, k, level, dx, "NULL")
    ####################### CHANGES STARTING HERE #####################
    # value and reference implemented like variable:
    elif k == "value":
        x = tableValue(id, k, level, dx, "NULL")
        dx += 1
    elif k == "reference":
        x = tableValue(id, k, level, dx, "NULL")
        dx += 1
    ####################### CHANGES ENDING HERE #####################
    table.append(x)
    return dx
#--------------CONST DECLARATION---------------------------
def constdeclaration(tx, level):
    global sym, id, num;
    if sym=="ident":
        getsym()
        if sym == "eql":
            getsym()
            if sym == "number":
                enter(tx, "const", level, "null")
                getsym()
            else:
                error(2)
        else:
            error(3)
    else:
        error(4)
#-------------VARIABLE DECLARATION--------------------------------------
def vardeclaration(tx, level, dx):
    global sym;
    if sym=="ident":
        dx = enter(tx, "variable", level, dx)
        getsym()
    else:
        error(4)
    return dx
#-------------BLOCK-------------------------------------------------------------
def block(tableIndex, level):
    global sym, id, codeIndx, codeIndx0;
    tx = [1]
    tx[0] = tableIndex
    tx0 = tableIndex
    dx = 3
    cx1 = codeIndx
    gen("JMP", 0 , 0)
    ####################### CHANGES STARTING HERE #####################
    if level > 0:
        if sym == "semicolon":
            getsym()
            pass
        else:
            if sym != "lparen":
                error(29)

            while True:
                getsym()
                if sym != "VAL" and sym != "REF":
                    error(38)
                savedSym = sym

                while True:
                    getsym()
                    if sym != "ident":
                        error(14)
                    
                    table[tx0].params.append(False)     # increasing size of the parameter list

                    if savedSym == "VAL":
                        dx = enter(tx, "value", level, dx)      # enter val in ST
                        table[tx0].params[dx-4] = False         # setting it to "False" in parameter list to symbolize being "value"
                    else:   # savedSym == "REF"
                        dx = enter(tx, "reference", level, dx)  # enter ref in ST
                        table[tx0].params[dx-4] = True          # setting it to "True" in parameter list to symbolize being "ref"
                    getsym()

                    if sym != "comma":
                        break
                    
                if sym != "semicolon":
                    break
            
            if sym != "rparen":
                error(22)
            getsym()

            if sym != "semicolon":
                error(10)
            getsym()
    ####################### CHANGES ENDING HERE #####################
    while sym == "PROCEDURE" or sym == "FUNCTION" or sym == "VAR" or sym == "CONST":
        if sym == "CONST":
            while True:               #makeshift do while in python
                getsym()
                constdeclaration(tx, level)
                if sym != "comma":
                    break
            if sym != "semicolon":
                error(10);
            getsym()
        if sym == "VAR":
            while True:
                getsym()
                dx = vardeclaration(tx, level, dx)
                if sym != "comma":
                    break
            if sym != "semicolon":
                error(10)
            getsym()
        while sym == "PROCEDURE" or sym == "FUNCTION":
            savedSym = sym   # save sym
            getsym()
            if sym == "ident":
                if savedSym == "PROCEDURE":
                    enter(tx, "procedure", level, codeIndx)
                elif savedSym == "FUNCTION":
                    enter(tx, "function", level, codeIndx)
                getsym()
            else:
                error(4)

            # REMOVED SEMICOLON FROM HERE AND MOVED IT TO THE TOP OF BLOCK

            block(tx[0], level+ 1)
        
            if sym != "semicolon":
                error(10)
            getsym()

    fixJmp(cx1, codeIndx)
    if tx0 != 0:
        table[tx0].adr = codeIndx
    codeIndx0 = codeIndx
    gen("INT", 0, dx)
    statement(tx[0], level, tx0)
    gen("OPR", 0, 0)
    #print code for this block
    printCode()
#--------------STATEMENT----------------------------------------
def statement(tx, level, tx0):
    global sym, id, num;
    if sym == "ident" or sym == "VAL" or sym == "REF":
        i = position(tx, id)
        if i==0:
            error(11)
        elif table[i].kind != "variable" and table[i].kind != "function"\
            and table[i].kind != "value" and table[i].kind != "reference":  # needs to accept value and reference as well
            error(36)
        savekind = table[i].kind    # save kind
        getsym()
        if sym != "becomes":
            error(13)
        getsym()
        expression(tx, level)
        ####################### CHANGES STARTING HERE #####################
        if savekind == "variable" or savekind == "value":       # if kind is variable or value
            gen("STO", level - table[i].level, table[i].adr)    # STO lev-table[i].level, table[i].adr
        elif savekind == "reference":                           # if kind if reference
            gen("STI", level - table[i].level, table[i].adr)    # STI lev-table[i].level, table[i].adr
        ####################### CHANGES ENDING HERE #####################
        elif i!= tx0:                                           # outside its body
            error(37)                                           # can't assign to this function here
        else:                                                   # if kind is function and in its body
            gen("STO", 0, -1)                                   # STO 0, -1
    elif sym == "CALL":
        getsym()
        if sym != "ident":
            error(14)
        i = position(tx, id)
        if i==0:
            error(11)
        if table[i].kind != "procedure":
            error(15)
        getsym()
        ####################### CHANGES STARTING HERE #####################
        if sym == "lparen":
            p = 0
            gen("INT", 0, 3)    # "fake" call

            while True:
                getsym()
                if table[i].params[p] == True:      # target is ref
                    if sym != "ident":
                        error(14)
                    j = position(tx, id)            # for getting ident types
                    if j == 0:
                        error(15)   # calling a constant

                    if table[j].kind == "variable" or table[j].kind == "value":         # if variable or value
                        gen("LDA", level - table[j].level, table[j].adr)                # LDA lev-table[i].level, table[i].adr
                    elif table[j].kind == "reference":                                  # if reference
                        gen("LOD", level - table[j].level, table[j].adr)                # LOD lev-table[i].level, table[i].adr
                    else:
                        error(10000000) # expected var/val/ref
                    getsym()
                else:                               # target is val
                    expression(tx, level)

                p += 1
                if sym != "comma":
                    break

            if sym != "rparen":
                error(22)
            gen("INT", 0, -(3 + p))                 # INT 0, -(3+p)
            getsym()
        
        gen("CAL", level - table[i].level, table[i].adr)    # CAL lev-table[i].level, table[i].adr
        ####################### CHANGES ENDING HERE #####################
    elif sym == "IF":
        getsym()
        generalExpression(tx, level)
        cx1 = codeIndx
        gen("JPC", 0, 0)
        if sym != "THEN":
            error(16)
        getsym()
        statement(tx, level, tx0)
        if sym == "ELSE":
            cx2 = codeIndx          # save cx2
            gen("JMP", 0, 0)        # JMP 0,0
            fixJmp(cx1, codeIndx)   # fix JPC @ cx1
            getsym()
            statement(tx, level, tx0)
            fixJmp(cx2, codeIndx)   # fix JMP @ cx2
        else:
            fixJmp(cx1, codeIndx)
    elif sym == "BEGIN":
        while True:
            getsym()
            statement(tx, level, tx0)
            if sym != "semicolon":
                break
        if sym != "END":
            error(17)
        getsym()
    elif sym == "WHILE":
        getsym()
        cx1 = codeIndx
        generalExpression(tx, level)
        cx2 = codeIndx
        gen("JPC", 0, 0)
        if sym != "DO":
            error(18)
        getsym()
        statement(tx, level, tx0)
        gen("JMP", 0, cx1)
        fixJmp(cx2, codeIndx)

    elif sym == "REPEAT":
        getsym()
        cx = codeIndx           # save cx

        while True:
            statement(tx, level, tx0)
            if sym != "semicolon":
                break
            getsym()

        if sym != "UNTIL":
            error(27)       # expects "until" reserved word
        getsym()

        generalExpression(tx, level)
        gen("JPC", 0, cx)       # JPC 0, cx

    elif sym == "FOR":
        getsym()
        if sym == "ident":
            i = position(tx, id)
            if i==0:                            # checking if the variable has been declared
                error(11)
            elif table[i].kind != "variable":   # checking if the variable is not constant
                error(12)

        if sym != "ident":
            error(4)        # expects identifier
        getsym()

        if sym != "becomes":
            error(13)       # expects "becomes"
        getsym()

        expression(tx, level)      # first expression

        gen("STO", level - table[i].level, table[i].adr)    # STO lev-table[i].level, table[i].adr

        if sym != "TO" and sym != "DOWNTO":
            error(28)       # expects either "to" or "downto"s after first expression
        savedSym = sym      # save sym
        getsym()

        expression(tx, level)      # second expression

        cx1 = codeIndx
        gen("CTS", 0, 0)    # CTS 0, 0
        gen("LOD", level - table[i].level, table[i].adr)    # LOD lev-table[i].level, table[i].adr

        if savedSym == "TO":
            gen("OPR", 0, 11)       # OPR 0, >=
        else:   # savedSym == "DOWNTO":
            gen("OPR", 0, 13)       # OPR 0, <=
        
        cx2 = codeIndx          # save cx2
        gen("JPC", 0, 0)        # JPC 0, 0

        if sym != "DO":
            error(18)       # expects "do"
        getsym()

        statement(tx, level, tx0)   # finish for loop with statement

        gen("LOD", level - table[i].level, table[i].adr)    # LOD lev-table[i].level, table[i].adr
        gen("LIT", 0, 1)

        if savedSym == "TO":
            gen("OPR", 0, 2)       # OPR 0, +
        else:   # savedSym == "DOWNTO":
            gen("OPR", 0, 3)       # OPR 0, -
        
        gen("STO", level - table[i].level, table[i].adr)    # STO lev-table[i].level, table[i].adr

        gen("JMP", 0, cx1)          # JMP 0, cx1
        fixJmp(cx2, codeIndx)       # fix JPC @ cx2
        gen("INT", 0, -1)           # INT 0, -1

    elif sym == "CASE":
     	getsym()
        expression(tx, level)
        if sym != "OF":
            error(30)
        getsym()

        firstCase = True;
        while sym == "number" or sym == "ident":
            gen("CTS", 0, 0)                    # CTS 0, 0
            if sym == "ident":
                i = position(tx, id)
                if i == 0:
                    error(11)
                if table[i].kind != "const":
                    error(25)
                gen("LIT", 0, table[i].value)   # LIT 0, table[i].value
            elif sym == "number":
                gen("LIT", 0, num)              # LIT 0, num

            getsym()
            gen("OPR", 0, 8)    # OPR 0, =
            cx1 = codeIndx      # save cx1
            gen("JPC", 0, 0)    # JPC 0, 0

            # check colon, call statement, check semicolon:
            if sym != "colon":
                error(31)
            getsym()

            statement(tx, level, tx0)

            if sym != "semicolon":
                error(32)
            getsym()

            # check if first case:
            if firstCase:
                firstCase = False
                cx2 = codeIndx
                gen("JMP", 0, 0)    # JMP 0, 0
            else:
                gen("JMP", 0, cx2)  # JMP 0, cx2
            fixJmp(cx1, codeIndx)   # fix JPC @ cx1

        if sym != "CEND":
            error(33)
        getsym()

        if not firstCase:
            fixJmp(cx2, codeIndx)
            gen("INT", 0, -1)

    
    elif sym == "WRITE" or sym == "WRITELN":
        savedSym = sym                  # save sym
        getsym()
        if sym != "lparen":
            error(29)                   # print statement needs left parenthesis
        getsym()

        while True:
            expression(tx, level)       # do while loop idea in python
            gen("OPR", 0, 14)           # OPR 0, W
            if sym != "comma":          # until no more expressions to print
                break
            getsym()
        
        if sym != "rparen":
            error(22)                   # expects right parenthesis
        getsym()
        
        if savedSym == "WRITELN":
            gen("OPR", 0, 15)           # OPR 0, WL

#--------------EXPRESSION--------------------------------------
def expression(tx, level):
    global sym;
    if sym == "plus" or sym == "minus":
        addop = sym
        getsym()
        term(tx, level)
        if (addop == "minus"):         #if minus sign, do negate operation
            gen("OPR", 0, 1)
    else:
        term(tx, level)
    
    while sym == "plus" or sym == "minus" or sym == "OR":
        addop = sym
        getsym()
        term(tx, level)
        
        if(addop == "plus" or addop == "OR"):
            gen("OPR", 0, 2)       # add and "or" operation
        else:
            gen("OPR", 0, 3)       # subtract operation  
#-------------TERM----------------------------------------------------
def term(tx, level):
    global sym;
    factor(tx, level)
    while sym=="times" or sym=="slash" or sym=="AND":
        mulop = sym
        getsym()
        factor(tx, level)
        if mulop == "times" or mulop == "AND":
            gen("OPR", 0, 4)         #multiply and "and" operation
        else:
            gen("OPR", 0, 5)         #divide operation
#-------------FACTOR--------------------------------------------------
def factor(tx, level):
    global sym, num, id;
    if sym == "ident" or sym == "VAL" or sym == "REF":
        i = position(tx, id)
        if i==0:
            error(11)
        if table[i].kind == "const":                                        # if constant
            gen("LIT", 0, table[i].value)                                   # LIT 0, table[i].val
        ####################### CHANGES STARTING HERE #####################
        elif table[i].kind == "variable" or table[i].kind == "value":       # if variable or value
            gen("LOD", level - table[i].level, table[i].adr)                # LOD lev-table[i].level, table[i].adr
        elif table[i].kind == "reference":                                  # if reference
            gen("LDI", level - table[i].level, table[i].adr)                # LDI lev-table[i].level, table[i].adr
        ####################### CHANGES ENDING HERE #####################
        elif table[i].kind == "procedure" or table[i].kind == "function":   # if procedure/function
            error(21)                                                       # error!
        getsym()
    elif sym == "number":
        gen("LIT", 0, num)
        getsym()
    elif sym == "lparen":
        getsym()
        generalExpression(tx, level)
        if sym != "rparen":
            error(22)
        getsym()
    elif sym == "CALL":
        getsym()
        if sym != "ident":
            error(14)
        i = position(tx, id)
        if i==0:
            error(11)
        if table[i].kind != "function":
            error(35)                                       # must be a function!
        gen("INT", 0, 1)                                    # INT 0, 1
        getsym()
        ####################### CHANGES STARTING HERE #####################
        if sym == "lparen":
            p = 0
            gen("INT", 0, 3)    # "fake" call

            while True:
                getsym()
                if table[i].params[p] == True:      # target is ref
                    if sym != "ident":
                        error(14)
                    j = position(tx, id)            # for getting ident types
                    if j == 0:
                        error(15)   # calling a constant

                    if table[j].kind == "variable" or table[j].kind == "value":         # if variable or value
                        gen("LDA", level - table[j].level, table[j].adr)                # LDA lev-table[i].level, table[i].adr
                    elif table[j].kind == "reference":                                  # if reference
                        gen("LOD", level - table[j].level, table[j].adr)                # LOD lev-table[i].level, table[i].adr
                    else:
                        error(10000000) ############# expected var/val/ref
                    getsym()
                else:                               # target is val
                    expression(tx, level)

                p += 1
                if sym != "comma":
                    break

            if sym != "rparen":
                error(22)
            gen("INT", 0, -(3 + p))                 # INT 0, -(3+p)
            getsym()
        
        gen("CAL", level - table[i].level, table[i].adr)    # CAL lev-table[i].level, table[i].adr
        ####################### CHANGES ENDING HERE #####################
    elif sym == "NOT":
        getsym()
        factor(tx, level)
        gen("LIT", 0, 0)    # LIT 0, 0
        gen("OPR", 0, 8)    # OPR 0, =
    else:
        error(24)
#-----------generalExpression-------------------------------------------------
def generalExpression(tx, level):
    global sym;
    if sym == "ODD":
        getsym()
        expression(tx, level)
        gen("OPR", 0, 6)
    else:
        expression(tx, level)
        if (sym in ["eql","neq","lss","leq","gtr","geq"]):
            temp = sym
            getsym()
            expression(tx, level)
            if temp == "eql":
                gen("OPR", 0, 8)
            elif temp == "neq":
                gen("OPR", 0, 9)
            elif temp == "lss":
                gen("OPR", 0, 10)
            elif temp == "geq":
                gen("OPR", 0, 11)
            elif temp == "gtr":
                gen("OPR", 0, 12)
            elif temp == "leq":
                gen("OPR", 0, 13)

#-------------------MAIN PROGRAM------------------------------------------------------------#

########################## added REFERENCE, VALUE
rword.append('AND')
rword.append('BEGIN')
rword.append('CALL')
rword.append('CASE')
rword.append('CEND')
rword.append('CONST')
rword.append('DO')
rword.append('DOWNTO')
rword.append('ELSE')
rword.append('END')
rword.append('FOR')
rword.append('FUNCTION')
rword.append('IF')
rword.append('NOT')
rword.append('ODD')
rword.append('OF')
rword.append('OR')
rword.append('PROCEDURE')
rword.append('REF')
rword.append('REPEAT')
rword.append('THEN')
rword.append('TO')
rword.append('UNTIL')
rword.append('VAL')
rword.append('VAR')
rword.append('WHILE')
rword.append('WRITE')
rword.append('WRITELN')

ssym = {'+' : "plus",
             '-' : "minus",
             '*' : "times",       
             '/' : "slash",
             '(' : "lparen",
             ')' : "rparen",
             '=' : "eql",
             ',' : "comma",
             '.' : "period",
             '#' : "neq",
             '<' : "lss",
             '>' : "gtr",
             '"' : "leq",
             '@' : "geq",
             ';' : "semicolon",
             ':' : "colon",}
charcnt = 0
whichChar = 0
linelen = 0
ch = ' '
kk = al                
a = []
id= '     '
errorFlag = 0
table.append(0)    #making the first position in the symbol table empty
sym = ' '       
codeIndx = 0         #first line of assembly code starts at 1
prevIndx = 0
infile =    sys.stdin       #path to input file
outfile =  sys.stdout     #path to output file, will create if doesn't already exist

getsym()            #get first symbol
block(0, 0)             #call block initializing with a table index of zero
if sym != "period":      #period expected after block is completed
    error(9)
print  
if errorFlag == 0:
    print >>outfile, "Successful compilation!\n"
    
Interpret()
