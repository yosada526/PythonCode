#!/usr/bin/env python

#CYPHER
strEnc = "AAMSMTFSCAIYTTOCGSEOMAMCRRELBE"

#Decode
def dec_scytale(c, k):
m = []
l = len(c)
for i in range(0,k):
for j in range(1,l+1):
if((j-1) % k == i):
m.append(c[j-1])
return "".join(m)

#Main
for n in range(2,len(strEnc)+1):
print(str(n) + " : " + dec_scytale(strEnc,n))
