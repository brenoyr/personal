#########################################################
#   Name:       Breno Yamada Riquieri                   #
#   Class:      CSC330 - Programming Languages          #
#   A:          Compiler Program #1                     #
#   Due Date:   24th January, 2020                      #
#                                                       #
#   Notes:      done so far: else, repeat-until, write, #
#               writeln, for, case, restricted globals  #
#                                                       #
#               COMPILES post-mod.pas SUCCESSFULLY      #
#               Handles error cases like it should      #
#########################################################
import sys

# increased norw from 11 to 22:
norw = 22      #number of reserved words
txmax = 100   #length of identifier table
nmax = 14      #max number of digits in number
al = 10          #length of identifiers

a = []
chars = []
rword = []
table = []

global infile, outfile, ch, sym, id, num, linlen, kk, line, errorFlag, linelen

class tableValue():
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

def error(num):
    global errorFlag;
    errorFlag = 1
    
    print
    if num == 1: 
        print >>outfile, "Use = instead of :="
    elif num ==2: 
        print >>outfile, "= must be followed by a number."
    elif num ==3: 
        print >>outfile, "Identifier must be followed by ="
    elif num ==4: 
        print >>outfile, "Const, Var, Procedure, For must be followed by an identifier."
    elif num ==5: 
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
    elif num ==25:
        print >>outfile, "Constant or Number is expected."
    elif num == 26: 
        print >>outfile, "This number is too large."
    ####################### CHANGES STARTING HERE #####################
    # new error cases:
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
    ####################### CHANGES ENDING HERE #####################
    exit(0)
    
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
        
def getsym():
    global charcnt, ch, al, a, norw, rword, sym, nmax, id
    while ch == " " or ch == "\n" or ch == "\r":
        getch()
    a = []
    if ch.isalpha():
        k = 0
        while True:
            a.append(ch)
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
            id = "".join(a)
    
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
def position(tx, k):
    global  table;
    table[0] = tableValue(k, "TEST")
    i = tx
    while table[i].name != k:
        i=i-1
    return i
#---------------ENTER PROCEDURE-------------------------------
def enter(tx, k):
    global id;
    tx[0] += 1
    while (len(table) > tx[0]):
      table.pop()
    x = tableValue(id, k)
    table.append(x)
#--------------CONST DECLARATION---------------------------
def constdeclaration(tx):
    global sym, id;
    if sym=="ident":
        temp = id
        getsym()
        if sym == "eql":
            getsym()
            if sym == "number":
                id = temp
                enter(tx, "const")
                getsym()
            else:
                error(2)
        else:
            error(3)
    else:
        error(4)

#-------------VARIABLE DECLARATION-----------------------------------
def vardeclaration(tx):
    global sym;
    if sym=="ident":
        enter(tx, "variable")
        getsym()
    else:
        error(4)
    
#-------------BLOCK------------------------------------------------
def block(tableIndex):
    tx = [1]
    tx[0] = tableIndex
    global sym, id;

    while sym == "CONST" or sym == "VAR" or sym == "PROCEDURE": # wrapping restricted globals
        if sym == "CONST":
            while True:               #makeshift do while in python
                getsym()
                constdeclaration(tx)
                if sym != "comma":
                    break
            if sym != "semicolon":
                error(10);
            getsym()
        
        if sym == "VAR":
            while True:
                getsym()
                vardeclaration(tx)
                if sym != "comma":
                    break
            if sym != "semicolon":
                error(10)
            getsym()
        
        while sym == "PROCEDURE":
            getsym()
            if sym == "ident":
                enter(tx, "procedure")
                getsym()
            else:
                error(4)
            if sym != "semicolon":
                error(10)
            getsym()
            block(tx[0])
            
            if sym != "semicolon":
                error(10)
            getsym()
    
    statement(tx[0])

#--------------STATEMENT----------------------------------------
def statement(tx):
    global sym, id;
    if sym == "ident":
        i = position(tx, id)
        if i==0:
            error(11)
        elif table[i].kind != "variable":
            error(12)
        getsym()
        if sym != "becomes":
            error(13)
        getsym()
        expression(tx)
        
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
    
    elif sym == "IF":
        getsym()
        condition(tx)
        if sym != "THEN":
            error(16)
        getsym()
        statement(tx)
        ####################### CHANGES STARTING HERE #####################
        if sym == "ELSE":
            getsym()
            statement(tx)   # simply call statement again for else
        ####################### CHANGES ENDING HERE #####################
    
    elif sym == "BEGIN":
        while True:
            getsym()
            statement(tx)
            if sym != "semicolon":
                break
        if sym != "END":
            error(17)
        getsym()
    
    elif sym == "WHILE":
        getsym()
        condition(tx)
        if sym != "DO":
            error(18)
        getsym()
        statement(tx)
    
    ####################### BEGIN ADDITIONAL FEATURES #####################
    elif sym == "FOR":
        getsym()
        forFunc(tx)
    
    # write and writeln work the same, at least for this first compiler's purposes:
    elif sym == "WRITE" or sym == "WRITELN":
        getsym()
        write(tx)
    
    elif sym == "REPEAT":
        getsym()
        repeat(tx)
    
    elif sym == "CASE":
        getsym()
        case(tx)
    ####################### END ADDITIONAL FEATURES #####################

#--------------EXPRESSION--------------------------------------
def expression(tx):
    global sym;
    if sym == "plus" or sym == "minus":
        getsym()
        term(tx)
    else:
        term(tx)
    
    while sym == "plus" or sym == "minus":
        getsym()
        term(tx)

#-------------TERM----------------------------------------------------
def term(tx):
    global sym;
    factor(tx)
    while sym=="times" or sym=="slash":
        getsym()
        factor(tx)

#-------------FACTOR--------------------------------------------------
def factor(tx):
    global sym;
    if sym == "ident":
        i = position(tx, id)
        if i==0:
            error(11)
        getsym()
    
    elif sym == "number":
        getsym()
    
    elif sym == "lparen":
        getsym()
        expression(tx)
        if sym != "rparen":
            error(22)
        getsym()
    
    else:
        error(24)

#-----------CONDITION-------------------------------------------------
def condition(tx):
    global sym;
    if sym == "ODD":
        getsym()
        expression(tx)
    
    else:
        expression(tx)
        if not (sym in ["eql","neq","lss","leq","gtr","geq"]):
            error(20)
        else:
            getsym()
            expression(tx)

####################### REPEAT #####################
def repeat(tx):
    global sym;

    while True:
        statement(tx)
        if sym != "semicolon":
            break
        getsym()

    if sym != "UNTIL":
        error(27)       # expects "until" reserved word
    getsym()

    condition(tx)

####################### WRITE and WRITELN #####################
def write(tx):
    global sym;


    if sym != "lparen":
        error(29)       # print statement needs left parenthesis
    getsym()

    while True:
        expression(tx)      # do while loop idea in python
        if sym != "comma":  # until no more expressions to print
            break
        getsym()
    
    if sym != "rparen":
        error(22)       # expects right parenthesis
    getsym()


####################### FOR #####################
def forFunc(tx):
    global sym;

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

    expression(tx)      # first expression

    if sym != "TO" and sym != "DOWNTO":
        error(28)       # expects either "to" or "downto" after first expression
    getsym()

    expression(tx)      # second expression

    if sym != "DO":
        error(18)       # expects "do"
    getsym()

    statement(tx)   # finish for loop with statement

####################### CASE #####################
def case(tx):
    global sym;

    expression(tx)

    if sym != "OF":
        error(30)       # expects "of"
    getsym()

    # execute loop if sym is a number or identifier:
    while sym == "number" or sym == "ident":    # works like the loops in expression and term
        if sym == "ident":
            i = position(tx, id)
            if i==0:                            # checking if the variable has been declared
                error(11)
            elif table[i].kind != "const":      # checking if the variable is constant
                error(34)

        getsym()

        if sym != "colon":
            error(31)       # expects ":"
        getsym()

        statement(tx)

        if sym != "semicolon":  # expects ";"
            error(32)
        getsym()
    
    if sym != "CEND":
        error(33)       # expects "cend"
    getsym()

#-------------------MAIN PROGRAM------------------------------------------------------------#

rword.append('BEGIN')
rword.append('CALL')
rword.append('CASE')        # new reserved word
rword.append('CEND')        # new reserved word
rword.append('CONST')
rword.append('DO')
rword.append('DOWNTO')      # new reserved word
rword.append('ELSE')        # new reserved word
rword.append('END')
rword.append('FOR')         # new reserved word
rword.append('IF')
rword.append('ODD')
rword.append('OF')          # new reserved word
rword.append('PROCEDURE')
rword.append('REPEAT')      # new reserved word
rword.append('THEN')
rword.append('TO')          # new reserved word
rword.append('UNTIL')       # new reserved word
rword.append('VAR')
rword.append('WHILE')
rword.append('WRITE')       # new reserved word
rword.append('WRITELN')     # new reserved word

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

infile =    sys.stdin       #path to input file
outfile =  sys.stdout     #path to output file, will create if doesn't already exist

getsym()            #get first symbol
block(0)             #call block initializing with a table index of zero

if sym != "period":      #period expected after block is completed
    error(9)
   
print >> outfile
if errorFlag == 0:
    print >>outfile, "Successful compilation!"
