#!/usr/bin/env python3
import string
import pprint

fo = open("txt_pico_enc_4.txt","r")
message = fo.read()
#read message from file

listAlpha = list(string.ascii_lowercase)
dicAlpha = {}
for c in listAlpha:
    dicAlpha[c] = 0

for d in message:
    if d in listAlpha:
        dicAlpha[d.lower()] += 1

#ソートキーに、配列2要素目を返すラムダ式をセットする。
#整然化出力で表示する。
pprint.pprint(sorted(dicAlpha.items(), key=lambda x:x[1],reverse=True)) 