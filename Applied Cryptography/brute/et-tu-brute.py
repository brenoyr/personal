#########################################################
#   Name:       Breno Yamada Riquieri                   #
#   Class:      CSC444 - Applied Cryptography           #
#   A:          Et tu, brute?                           #
#   Due Date:   03/23/2020                              #
#                                                       #
#########################################################

from sys import stdin

# the alphabet
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:'\",<.>/? "
#ALPHABET = " -,;:!?/.'\"()[]$&#%012345789aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxyYzZ"

THRESHOLD = 0.75

# the dictionary
DICTIONARY_FILE = "dictionary.txt"

# performs a ROT
def rot(ciphertext, shift):
    rotatedcipher = ""

    for line in ciphertext:                                 # get a line in the ciphertext
        cipherline = list(line)                             # work with that line as a list

        for i in range (0, len(cipherline)):                # loop through every character
            alphabetIndex = ALPHABET.find(cipherline[i])    # find the index of the current letter in our alphabet
            rotIndex = alphabetIndex + shift                # rotation index the current letter's index + shift

            if (rotIndex >= len(ALPHABET)):                 # if rotIndex is bigger than alphabet's length, just
                rotIndex -= len(ALPHABET)                   # subtract to loop back to the beginning of the alphabet
            
            cipherline[i] = ALPHABET[rotIndex]              # substitute letter for the shifted letter

        rotatedcipher += "".join(cipherline)
        rotatedcipher += "\n"
    
    return rotatedcipher

# read in the dictonary:
f = open(DICTIONARY_FILE, "r")
dictionary = f.read().rstrip("\n").lower().strip("\n")
f.close()

ciphertext = stdin.read().rstrip("\n")
ciphertext = ciphertext.split("\n")[:10]    #################### dont forget to change this
#print ciphertext

# apply rotations through the entire alphabet:
for i in range (1, len(ALPHABET)):
    
    # print "\n\n", i
    plaintext = rot(ciphertext, i)
    words = plaintext.split(" ")

    # checking if the words in the plaintext match words in the dictionary:
    count = 0
    for word in words:
        validWord = ""

        for w in word:
            if w.isalpha():
                validWord = "".join([validWord, w]).lower()
        #print validWord
        if validWord in dictionary.lower():
            count += 1

    # print count, i
    # if enough words match word in the dictionary:
    if (count > len(words) * THRESHOLD):
        print "Shift is {}\nPlaintext: {}".format(95-i, plaintext)
        # print "Shift is {}\nPlaintext: {}".format(95-i, "".join(words))