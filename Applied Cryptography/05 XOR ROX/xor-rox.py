#   Name:       Breno Yamada Riquieri                   #
#   Class:      CSC444 - Applied Cryptography           #
#   A:          XOR ROX                                 #
#   Due Date:   05/05/2020                              #
#   Comments:   Python 2.7.17                           #
#                                                       #
#########################################################

# XOR ROX
# Sample template to show how to manipulate PNG pixels
# Also includes default values for the input and output image filenames
#  (keep them that way!)

from PIL import Image

from random import randint

RGB_RANGE = 256

# the images
INPUT_IMAGE = "input.png"
AND_IMAGE = "and.png"
OR_IMAGE = "or.png"
XOR_IMAGE = "xor.png"

# get the input image
img_for_and = Image.open(INPUT_IMAGE)
img_for_or = Image.open(INPUT_IMAGE)
img_for_xor = Image.open(INPUT_IMAGE)

pixels_and = img_for_and.load()
pixels_or = img_for_or.load()
pixels_xor = img_for_xor.load()

rows, cols = img_for_and.size


# pick some pixels to change
for row in range(0, rows):
    for col in range(0, cols):
        # get the current pixel
        r, g, b = pixels_and[row, col]

        # generate and display the key pixel RGB values
        key_r = randint(0, 255)
        key_g = randint(0, 255)
        key_b = randint(0, 255)
        print "{},{},{}".format(key_r, key_g, key_b)

        # change the current pixel RGB values for AND
        and_r = r & key_r
        and_g = g & key_g
        and_b = b & key_b

        pixels_and[row, col] = (and_r, and_g, and_b)

        # change the current pixel RGB values for OR
        or_r = r | key_r
        or_g = g | key_g
        or_b = b | key_b

        pixels_or[row, col] = (or_r, or_g, or_b)
        

        # change the current pixel RGB values for XOR
        xor_r = r ^ key_r
        xor_g = g ^ key_g
        xor_b = b ^ key_b

        pixels_xor[row, col] = (xor_r, xor_g, xor_b)



# write the new image
img_for_and.save(AND_IMAGE)
img_for_or.save(OR_IMAGE)
img_for_xor.save(XOR_IMAGE)