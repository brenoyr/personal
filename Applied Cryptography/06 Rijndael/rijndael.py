#   Name:       Breno Yamada Riquieri                   #
#   Class:      CSC444 - Applied Cryptography           #
#   A:          Rijndael                                #
#   Due Date:   05/08/2020                              #
#   Comments:   Python 2.7.17                           #
#														#
#               Ciphertexts 1-5 working                 #
#########################################################

from sys import stdin, stdout, stderr
from re import sub
from hashlib import sha256
from Crypto import Random
from Crypto.Cipher import AES

# the AES block size to use
BLOCK_SIZE = 16

# the padding character to use to make the plaintext a multiple of BLOCK_SIZE in length
PAD_WITH = "#"

# set the dictionary
DICTIONARY = "dictionary1-3.txt"
# DICTIONARY = "dictionary4.txt"
# DICTIONARY = "dictionary5.txt"

# threshold and minimum word length
THRESHOLD = 0.5
MIN_WORD_LEN = 3

# hint from watching the video.
# process the dictionary in reverse order.
# ciphertext 3 benefits from this since its
# key is closer to the end of the dictionary
REVERSE = False

# set dictionary filter.
# hint for ciphertext 4 was that
# the key started with either "J" or "j"
FILTER = []
# FILTER = ["J", "j"]

# look for a specific tag at the beginning of candidate plaintext?
USE_TAG = False
TAG = "%PDF-1.4"

# set to True to write key to stderr.
# send output to a temp file and then
# only the key will be shown in terminal
SPIT_KEY = True

# set to True to stop after finding a candidate plaintext
BREAK = True

# decrypts a ciphertext with a key
def decrypt(ciphertext, key):
	# hash the key (SHA-256) to ensure that it is 32 bytes long
	key = sha256(key).digest()
	# get the 16-byte IV from the ciphertext
	# by default, we put the IV at the beginning of the ciphertext
	iv = ciphertext[:16]

	# decrypt the ciphertext with the key using CBC block cipher mode
	cipher = AES.new(key, AES.MODE_CBC, iv)
	# the ciphertext is after the IV (so, skip 16 bytes)
	plaintext = cipher.decrypt(ciphertext[16:])

	# remove potential padding at the end of the plaintext.
	# if there's padding (which means at least the last char
	# in the string is PAD_WITH), check how many by going backwards.
	# once we know where the padding starts, adjust the plaintext
	if plaintext[-1] == PAD_WITH:
		cur = -1
		length = len(plaintext)
		while plaintext[cur] == PAD_WITH:
			cur -= 1
			length -= 1
		plaintext = plaintext[:length]

	return plaintext

# encrypts a plaintext with a key
def encrypt(plaintext, key):
	# hash the key (SHA-256) to ensure that it is 32 bytes long
	key = sha256(key).digest()
	# generate a random 16-byte IV
	iv = Random.new().read(BLOCK_SIZE)

	# encrypt the ciphertext with the key using CBC block cipher mode
	cipher = AES.new(key, AES.MODE_CBC, iv)
	# if necessary, pad the plaintext so that it is a multiple of BLOCK SIZE in length
	plaintext += (BLOCK_SIZE - len(plaintext) % BLOCK_SIZE) * PAD_WITH
	# add the IV to the beginning of the ciphertext
	# IV is at [:16]; ciphertext is at [16:]
	ciphertext = iv + cipher.encrypt(plaintext)

	return ciphertext

# MAIN

# read in the dictonary (for keywords)
f = open(DICTIONARY, "r")
dictionary = f.read().rstrip("\n").split("\n")
f.close()

# read in the dictonary (for comparing normalized words)
f = open(DICTIONARY, "r")
lower_dictionary = f.read().rstrip("\n").lower().split("\n")
f.close()

# reverse dictionary if desired
# note that we don't need to reverse
# the dictionary used for comparing normalized words
# (it would be redundant)
if REVERSE:
	dictionary.reverse()

# read in the ciphertext
ciphertext = stdin.read().rstrip("\n")

for keyword in dictionary:
    # check if we should filter
	if FILTER:
		if keyword[0] not in FILTER:
			continue

	# decrypt plaintext and split it into words
	plaintext = decrypt(ciphertext, keyword)
	words = plaintext.split(" ")

	# if we are looking for a tag
	if USE_TAG:
		# found candidate plaintext 
		# if it finds that tag at the
		# start of the plaintext file
		# (redirecting output to a file
		# will still print key to stdout)
		if TAG in words[0]:
			stderr.write("KEY={}\n".format(keyword))
			stdout.write("{}\n".format(plaintext))
			exit(0)
	else:
		# checking if the words in the plaintext match words in the dictionary
		# (they also need to satisfy the minimum word length):
		count = 0
		for word in words:
			# removing punctuation from the word
			normalized = sub(r'[^\w]+','', word).lower()

			if normalized in lower_dictionary and len(normalized) >= MIN_WORD_LEN:
				count += 1

		if count > len(words) * THRESHOLD:
			if SPIT_KEY:
				stderr.write("KEY={}\n".format(keyword))
				stdout.write("{}\n".format(plaintext))
			else:
				stdout.write("KEY={}:\n{}\n".format(keyword, plaintext))
			
			if BREAK:
				exit(0)
