#!/usr/bin/env python

#CYPHER
#strEnc = "cfp"
#strKey = "code"
#strEnc = "pohzCZK{g1gt3w3_n1pn3wd_ax3s7_maj_1h7m92d3}"
#strKey = "agfl"
strEnc = "Yse lncsz bplr-izcarpnzjo dkxnroueius zf g uzlefwpnfmeznn"
strKey = "flag"
strMes = []

#Deconde
i = 0
m =""
for c in strEnc:
    if('a' <= c and c <= 'z'):
        strMes.append(chr((ord(c) - ord(strKey[i % len(strKey)])) % 26 + ord('a')))
        i+=1       
    elif('A' <= c and c <= 'Z'):
        strMes.append(chr((ord(c) - ord(strKey[i % len(strKey)].upper())) % 26 + ord('A')))
        i+=1
    else:
        strMes.append(c)


print("".join(strMes))
