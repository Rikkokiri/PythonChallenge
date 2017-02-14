# -*- coding: utf-8 -*-
# Python challenge
#### Challenge 6 ######

# http://www.pythonchallenge.com/pc/def/channel.html

from __future__ import print_function
import re
import os
import zipfile

archieveName = 'channel.zip'

def findNext(number):

    file = open('channel/%s.txt' % number)
    fileContent = file.read()
    file.close()
    nextNumber = re.findall(r'\d+', fileContent)

    if(len(nextNumber) == 1):
        print("From %s.txt found %s" % (number, nextNumber[0]))
        findNext(nextNumber[0])

    else:
        print("More or less than one number found in file %s: %s" % (number, fileContent))


def listComments():
    for info in zf.infolist():
        result += info.comment

    print(result)


def findNextWithComments(number):

    print(zf.getinfo('%s.txt' % number).comment, end="")

    file = zf.open('%s.txt' % number)
    fileContent = file.read()
    file.close()
    nextNumber = re.findall(r'\d+', fileContent)

    if(len(nextNumber) == 1):
        findNextWithComments(nextNumber[0])

    else:
        print("More or less than one number found in file %s: %s" % (number, fileContent))



# hint1: start from 90052
#findNext(90052)
# Result: in file 46145: "Collect the comments."

zf = zipfile.ZipFile(archieveName)
findNextWithComments(90052)
