#!/usr/bin/env python

#CYPHER
#strEnc = "BCD"
strEnc = "YNRJKQNJXQNPJFSFWWTB"

#Decode
def dec_caesar(c, n):
m = []
for cha in c:
if('A' <= cha and cha <= 'Z'):
m.append(chr((ord(cha) - ord('A') - n) % 26 + ord('A')))

else:
m.append(cha)
return "".join(m)

#Main
for n in range(1,25):
print(str(n) + " : " + dec_caesar(strEnc,n))
