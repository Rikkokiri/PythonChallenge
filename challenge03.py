# -*- coding: utf-8 -*-
# Python challenge
#### Challenge 3 ######

# Solution: "linkedlist"

'''
This solution is overly complex. The level should rather be solved with a regex statement.
'''

file = open('level3.txt')
text = file.read()

fUpper = 0
lower = 0
sUpper = 0

fletter = ""
mletter = ""
slettter = ""

m = "m"

for letter in text:
    if(fUpper == 3 and lower == 1 and sUpper == 3 and letter.islower()):

        print(fletter + mletter + sletter)

        fUpper = 0
        lower = 0
        sUpper = 0
        fletter = ""
        mletter = ""
        sletter = ""

    else:
        if(letter.isupper()):
            if(fUpper >= 3 and lower == 0):
                fUpper = fUpper + 1
            elif(fUpper == 3 and lower == 1):
                sUpper = sUpper + 1
                sletter = sletter + letter
            elif(fUpper < 3 and lower == 0 and sUpper == 0):
                fUpper = fUpper + 1
                fletter = fletter + letter
            else:
                fUpper = 0
                lower = 0
                sUpper = 0

                fletter = ""
                mletter = ""
                sletter = ""

        elif(letter.islower()):
            if(fUpper == 3 and lower == 0 and sUpper == 0):
                lower += 1
                mletter = mletter + letter
            else:
                fUpper = 0
                lower = 0
                sUpper = 0

                fletter = ""
                mletter = ""
                sletter = ""
