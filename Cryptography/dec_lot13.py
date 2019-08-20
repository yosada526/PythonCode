#!/usr/bin/env python

#CYPHER
#strEnc = "BCD"
#strEnc = "cvpbPGS{guvf_vf_pelcgb!}"
strEnc = "vgefmsaapaxpomqemdoubtqdxoaxypeo"

#Decode
def dec_caesar(c, n):
m = []
for cha in c:
if('A' <= cha and cha <= 'Z'):
m.append(chr((ord(cha) - ord('A') - n) % 26 + ord('A')))

elif('a' <= cha and cha <= 'z'):
m.append(chr((ord(cha) - ord('a') - n) % 26 + ord('a')))

else:
m.append(cha)
return "".join(m)

#Main
for n in range(1,25):
print(str(n) + " : " + dec_caesar(strEnc,n))
