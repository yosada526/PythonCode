#!/usr/bin/env python3
# coding: utf-8
"""python script
"""

import Crypto.Cipher.AES as AES
import Crypto.Random as Random
import json
import base64
BLOCK_SIZE = 16  # Bytes
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

#original_cookie
cookie = "Qrww774cECgh54L3FqjpMu+r4JscvFIuaC7G9NCseYc2Hht/1sEShJI828VfIryBp8ZAxkEtrGkIUWSz0qdGgNFbwhBRe+a70RnybtKrQfE="

def main():
    print("org_cookie:" + cookie)

    mod_cookie = mod_adminflg(cookie)

    print("mod_cookie:" + mod_cookie)

   

def mod_adminflg(org_cookie):
    
    dec_encrypted = base64.b64decode(org_cookie)

    FLIP_POS = 11

    flipped = bytes([dec_encrypted[FLIP_POS-1] ^ ord('0') ^ ord('1')])

    print( bytes([dec_encrypted[FLIP_POS -1]]) + b'is flipped to: ' + flipped)

    mod_data = []
    for i in range(len(dec_encrypted)):
        if i != FLIP_POS-1:
            mod_data.append(bytes([dec_encrypted[i]]))
        else:
            mod_data.append(flipped)
     
    mod_cookie = base64.b64encode(b''.join(mod_data))
 
    return mod_cookie.decode('ascii')


if __name__ == '__main__':
    main()