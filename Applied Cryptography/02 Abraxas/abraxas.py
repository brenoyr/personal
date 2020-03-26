#########################################################
#   Name:       Breno Yamada Riquieri                   #
#   Class:      CSC444 - Applied Cryptography           #
#   A:          Abraxas                                 #
#   Due Date:   03/27/2020                              #
#   Comments:                                           #
#########################################################

from sys import stdin

# the alphabet
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:'\",<.>/? "
# ALPHABET = " -,;:!?/.'\"()[]$&#%012345789aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxyYzZ"

# the threshold. 0.5 works well together with considering a word "valid" iff len(word) > 3
THRESHOLD = 0.5

# set the dictionary
DICTIONARY_FILE = "dictionary.txt"

def decrypt(ciphertext, keyword):
    plaintext = ""

    return plaintext


# this isUniqueChars function was copied from GeeksforGeeks.com.
# if returns true if a string has all unique characters; false otherwise.
# link: https://www.geeksforgeeks.org/python-program-to-check-if-a-string-contains-all-unique-characters/
def isUniqueChars(st): 
  
    # String length cannot be more than 
    # 256. 
    if len(st) > 256: 
        return False
  
    # Initialize occurrences of all characters 
    char_set = [False] * 128
  
    # For every character, check if it exists 
    # in char_set 
    for i in range(0, len(st)): 
  
        # Find ASCII value and check if it 
        # exists in set. 
        val = ord(st[i]) 
        if char_set[val]: 
            return False
  
        char_set[val] = True
  
    return True


# read in the dictonary:
f = open(DICTIONARY_FILE, "r")
dictionary = f.read().rstrip("\n").strip("\n")
f.close()

dictionaryList = dictionary.split("\n")

ciphertext = stdin.read().rstrip("\n")
ciphertext = ciphertext.split("\n")

for keyword in dictionaryList:
    if isUniqueChars(keyword):
        plaintext = decrypt(ciphertext, keyword)
#         if plaintext is valid: #meaning it passed the threshold
#             print plaintext


