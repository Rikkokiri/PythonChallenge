# -*- coding: utf-8 -*-
# Python challenge
#### Challenge 7 ######

# http://www.pythonchallenge.com/pc/def/oxygen.html

from PIL import Image
import re

img = Image.open('resources/oxygen.png')

# Get the center row of pixels
pixelrow = [img.getpixel((x, img.height / 2)) for x in range(img.width)]

# To eliminate duplicates, take every 7th pixel (each section 7 pixels wide)
pixelrow = pixelrow[0::7]

# Get the value for each grayscale pixel (condition in the end filters out colored pixels)
asc = [red for red, green, blue, alpha in pixelrow if red == green == blue]

# Map the obtained values to ASCII characters
sentence = "".join(map(chr, asc))

# Print the result
print(sentence) # => smart guy, you made it. the next level is [105, 10, 16, 101, 103, 14, 105, 16, 121]

# Get the numbers from the sentence
nums = re.findall("\d+", sentence)

# Map the obtained numbers to ASCII characters
answer = "".join(map(chr, map(int, nums)))

# Print the final result
print(answer)
