#########################################################
#   Name:       Breno Yamada Riquieri                   #
#   Class:      CSC444 - Applied Cryptography           #
#   A:          Abraxas                                 #
#   Due Date:   03/27/2020                              #
#   Comments:   Python 2.7.17                           #
#########################################################

from sys import stdin

# the alphabet
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:'\",<.>/? "
ALPHABET = " -,;:!?/.'\"()[]$&#%012345789aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxyYzZ"

# the threshold and minimum length for a word to be considered "valid"
THRESHOLD = 0.3
MIN_WORD_LEN = 4

# set the dictionary
DICTIONARY_FILE = "dictionary.txt"

def decrypt(ciphertext, keyword):
    plaintext = ""

    # here it gets messy, but I'm deleting characters in the key from the alphabet.
    # this is done with translate(), which is working in Unicode (therefore unicode(ALPHABET))
    # translate() takes the ordinal value replaces it with another value in a string.
    # if used with "None," a character deletion step is performed.
    # wrap things up with str() to bring it back to the desired string type,
    # then preppend the keyword to obtain the ciphertext alphabet:
    CIPHER_ALPHABET = keyword + str(unicode(ALPHABET).translate({ord(i): None for i in keyword}))

    for line in ciphertext:                                         # get a line in the ciphertext
        cipherLine = list(line)                                     # work with that line as a list

        for i in range (0, len(cipherLine)):                        # loop through every character
            alphabetIndex = CIPHER_ALPHABET.find(cipherLine[i])     # find the index in the original alphabet

            cipherLine[i] = ALPHABET[alphabetIndex]                 # substitute cipher letter for the original letter
        
        plaintext += "".join(cipherLine)
        plaintext += "\n"

    return plaintext


# this isUniqueChars function was taken from GeeksforGeeks.com.
# it returns true if a string has all unique characters; false otherwise.
# link: https://www.geeksforgeeks.org/python-program-to-check-if-a-string-contains-all-unique-characters/
def isUniqueChars(st): 
  
    # String length cannot be more than 256
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

        words = plaintext.split(" ")

        count = 0
        for word in words:
            if word in dictionary and len(word) >= MIN_WORD_LEN:
                count += 1

        if count >  len(words) * THRESHOLD:
            print "KEY={}:\n{}".format(keyword, plaintext)

