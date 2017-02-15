# -*- coding: utf-8 -*-
# Python challenge
#### Challenge 4 ######

# http://www.pythonchallenge.com/pc/def/linkedlist.php

# Accidentally found solution: peak.html

import urllib

phrase = "and the next nothing is "
starturl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"
baseurl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="


def findNext(url):

    page = urllib.urlopen(url)
    raw_data = page.read()

    print(raw_data)
    number = raw_data.rsplit(' ', 1)[1] #Maximum one splits on ' ' (performed starting from the right), get the latter one
    findNext(baseurl + number)


#findNext(baseurl)
findNext(baseurl+'8022') # Divide 16044 by 2 and keep going
