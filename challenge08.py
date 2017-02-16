# -*- coding: utf-8 -*-
# Python challenge
#### Challenge 8 ######

# http://www.pythonchallenge.com/pc/def/integrity.html

import bz2

un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

decoded_un = bz2.decompress(un)
decoded_pw = bz2.decompress(pw)

print("Username: " + decoded_un)
print("Password: " + decoded_pw)
