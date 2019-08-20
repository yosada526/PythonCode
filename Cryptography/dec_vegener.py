#!/usr/bin/env python

#CYPHER
#strEnc = "cfp"
#strKey = "code"
strEnc = "llkjmlmpadkkc"
strKey = "thisisalilkey"
strMes = []

#Deconde
for i in range(0,len(strEnc)):
    strMes.append(chr((ord(strEnc[i]) - ord(strKey[i])) % 26 + ord('a')))

print("".join(strMes))
