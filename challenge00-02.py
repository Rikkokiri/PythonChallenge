# -*- coding: utf-8 -*-
# Python challenge
# chellenges 1 - 2

# ------------- Challenge 0 -------------
print(2**38)

from string import maketrans


# ------------- Challenge 1 -------------

frm = 'abcdefghijklmnopqrstuvwxyz'
to = 'cdefghijklmnopqrstuvwxyzab'
transtable = maketrans(frm, to)

riddle = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print(riddle.translate(transtable))
print('map'.translate(transtable))


# ------------- Challenge 2 -------------

from collections import Counter

file = open('level2.txt')
mess = file.read()

#https://docs.python.org/3.6/library/collections.html#collections.Counter
counter = Counter()

for char in mess:
    counter[char] += 1

print(counter)
#print list(counter.elements())

#http://codereview.stackexchange.com/questions/94385/keeping-just-the-rare-characters-in-a-long-string
## ?????
s = ''.join(char for char in mess if counter[char] < 3)
print(s)
