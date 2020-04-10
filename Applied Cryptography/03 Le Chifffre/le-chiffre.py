#########################################################
#   Name:       Breno Yamada Riquieri                   #
#   Class:      CSC444 - Applied Cryptography           #
#   A:          Le Chiffre                              #
#   Due Date:   04/17/2020                              #
#   Comments:   Python 2.7.17                           #
#########################################################

from sys import stdin
import re

# the alphabet
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:'\",<.>/? "
ALPHABET = " -,;:!?/.'\"()[]$&#%012345789aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxyYzZ"

# the threshold and minimum length for a word to be considered "valid"
# 0.5 & 2 works for the assignment ciphertexts
# 0.3 & 2 works for the doubly encrypted message
THRESHOLD = 0.5
MIN_WORD_LEN = 2

DEBUG = False

# set the dictionary
DICTIONARY_FILE = "dictionary.txt"

# generates/lines up message and key
# Ex: [T,h,i,s,i,s,t,h,e,M,e,s,s,a,g,e]
#     [L,e,m,o,n,L,e,m,o,n,L,e,m,o,n,L]
# Taken from GeeksForGeeks.com at
# https://www.geeksforgeeks.org/vigenere-cipher/
def generateKey(ciphertext, key):
    key = list(key)
    if len(ciphertext) == len(key):
        return(key)
    else:
        # only mod from it's original version was subtracting:
        # 1 from the range calculation
        for i in range(len(ciphertext) - len(key) - 1):
            key.append(key[i % len(key)])
    return("".join(key))

# function that applies the vigenere decipher on a keyword:
def originalText(ciphertext, keyString):
    plaintext = ""
    keyTextIndex = 0
    ciphertext = ciphertext.split("\n")                             # make ciphertext a list of lines and loop through them
    for line in ciphertext:                                         # get a line in the ciphertext
        cipherLine = list(line)                                     # work with that line as a list

        for i in range (0, len(cipherLine)):                        # loop through every character
            # find the index in the original alphabet:
            # original index = index in old/ciphered text - index in key:
            cipher_index = ALPHABET.find(cipherLine[i])             # index in old/ciphered text
            key_index = ALPHABET.find(keyString[keyTextIndex])      # index in key
            keyTextIndex += 1                                       # IMPORTANT: update current index in our keyString
            plain_index = cipher_index - key_index
            plaintext += ALPHABET[plain_index % len(ALPHABET)]      # append original/plain char, which is gotten with
                                                                    # mod len(ALPHABET) to keep our index within the alphabet

        plaintext += "\n"                                           # done with a line, append "\n" and go to the next one

    return("".join(plaintext))

########## MAIN ##########

# read in the dictonary:
f = open(DICTIONARY_FILE, "r")
dictionary = f.read().rstrip("\n").split("\n")
f.close()

# keeping this as a comment in case it becomes helpful with a different dictionary:
# dictionary = [ re.sub(r"[^\w]+", "", x) for x in dictionary ]

ciphertext = stdin.read().rstrip("\n")
ciphertext = "\n".join(ciphertext.split("\n")[:10])

# checking every word in the dictionary for a possible valid key:
for keyword in dictionary:
    key = generateKey(ciphertext, keyword)

    if (DEBUG):
        # regex that deletes any (greedy) char that is not a-z or A-Z
        # note: using either r"[^a-zA-z]+" or r"[^\w]+" works for this assignment
        # NOTE TO SELF: maybe r"[^\w]+" will work better for the challenge so use that as default
        plain_keyword = re.sub(r'[^\w]','', keyword)

    plaintext = originalText(ciphertext, key)
    # checking if the words in the plaintext match words in the dictionary
    # (they also need to satisfy the minimum word length):
    words = plaintext.split(" ")
    count = 0
    for word in words:
        if len(word) >= MIN_WORD_LEN and word in dictionary:
            count += 1

    # if enough words match word in the dictionary:
    if count >  len(words) * THRESHOLD:
        print "KEY={}:\n{}".format(keyword, plaintext)