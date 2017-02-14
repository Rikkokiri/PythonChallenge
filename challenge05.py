# -*- coding: utf-8 -*-
# Python challenge
#### Challenge 5 ######

# http://www.pythonchallenge.com/pc/def/peak.html

from __future__ import print_function
import pickle


# Open the file for reading
f = open('level5.p', 'r')

# load the object from the file into var b
matrix = pickle.load(f)
f.close()

for row in matrix:
    #print row
    rowstring = ""

    for cell in row:
        print(cell[0]*cell[1], end='')
    print()
