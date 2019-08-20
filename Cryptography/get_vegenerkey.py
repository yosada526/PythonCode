#!/usr/bin/env python

#CYPHER
#pohzCZK{g1gt3w3_n1pn3wd_ax3s7_maj_1h7m92d3}
strC = "pohzCZK"
#Flugment of Message
strFlgM = "picoCTF"

#key agflagf
strKey = []
for i in range(len(strC)):
    strKey.append(chr(ord(strC[i]) - ord(strFlgM[i]) + ord('a')))

print("".join(strKey))



#Deconde
#for i in range(0,len(strEnc)):
#    strMes.append(chr((ord(strEnc[i]) - ord(strKey[i])) % 26 + ord('a')))

#print("".join(strMes))
