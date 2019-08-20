#!/usr/bin/env python

#Message
m = 0b10101010
key = 0b00001111

enc = m ^ key
print("enc:" + format(enc, 'b'))

dec = enc ^ key
print("dec:" + format(dec, 'b'))
