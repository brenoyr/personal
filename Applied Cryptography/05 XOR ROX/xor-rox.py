#   Name:       Breno Yamada Riquieri                   #
#   Class:      CSC444 - Applied Cryptography           #
#   A:          XOR ROX                                 #
#   Due Date:   05/05/2020                              #
#   Comments:   Python 2.7.17                           #
#                                                       #
#               Encrypt and Decrypt working             #
#                                                       #
#               The key file is read from stdin         #
#########################################################

# XOR ROX
# Sample template to show how to manipulate PNG pixels
# Also includes default values for the input and output image filenames
#  (keep them that way!)

from PIL import Image
from sys import stdin
from random import randint

# mode
DECRYPT = False
# DECRYPT = True

# the images
INPUT_IMAGE = "input.png"
AND_IMAGE = "and.png"
OR_IMAGE = "or.png"
XOR_IMAGE = "xor.png"
DECRYPTED_IMAGE = "decrypted.png"

# Encryption
if (DECRYPT == False):
    # get the input image
    img_for_and = Image.open(INPUT_IMAGE)
    img_for_or = Image.open(INPUT_IMAGE)
    img_for_xor = Image.open(INPUT_IMAGE)

    # load pixels for each
    pixels_and = img_for_and.load()
    pixels_or = img_for_or.load()
    pixels_xor = img_for_xor.load()

    # currently they are all the same so
    # we can get rows and cols from any of them
    rows, cols = img_for_xor.size

    # go through every pixel
    for row in range(0, rows):
        for col in range(0, cols):
            # get the current pixel
            # all 3 are still the same so get rgb from any
            r, g, b = pixels_xor[row, col]

            # generate and display the key pixel RGB values
            key_r = randint(0, 255)
            key_g = randint(0, 255)
            key_b = randint(0, 255)
            print "{},{},{}".format(key_r, key_g, key_b)

            # change the current pixel RGB values for AND
            and_r = r & key_r
            and_g = g & key_g
            and_b = b & key_b

            # change the current pixel RGB values for OR
            or_r = r | key_r
            or_g = g | key_g
            or_b = b | key_b

            # change the current pixel RGB values for XOR
            xor_r = r ^ key_r
            xor_g = g ^ key_g
            xor_b = b ^ key_b

            # overwrite pixels with the new rgb values
            pixels_and[row, col] = (and_r, and_g, and_b)
            pixels_or[row, col] = (or_r, or_g, or_b)
            pixels_xor[row, col] = (xor_r, xor_g, xor_b)

    # write the new image
    img_for_and.save(AND_IMAGE)
    img_for_or.save(OR_IMAGE)
    img_for_xor.save(XOR_IMAGE)
    exit(0)

# Decryption
else:
    # read the key file
    key = ciphertext = stdin.read().rstrip("\n")

    # make it into a list of rgb values
    key = key.split("\n")

    # get the xor'ed image
    img = Image.open("xor.png")

    # load pixels
    pixels = img.load()

    # get it's rows and cols numbers
    rows, cols = img.size
    
    # counter to loop through the list of key values
    i = 0

    # pick some pixels to change
    for row in range(0, rows):
        for col in range(0, cols):
            # get the current pixel's rgb values
            xor_r, xor_g, xor_b = pixels[row, col]

            # get the key used to encrypt
            key_r, key_g, key_b = key[i].split(',')

            # str -> int
            key_r = int(key_r)
            key_g = int(key_g)
            key_b = int(key_b)
            
            # increment counter to go to the next key values in the next loop
            i += 1

            # recover the original rgb values
            r = xor_r ^ key_r
            g = xor_g ^ key_g
            b = xor_b ^ key_b

            # overwrite pixels with the original rgb values
            pixels[row, col] = (r, g, b)
    
    # write the new decrypted image
    img.save(DECRYPTED_IMAGE)
    exit(0)
