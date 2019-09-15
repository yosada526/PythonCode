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


def main():
    """main
    """
    #key define
    #key = b'seed removed'
    key = b'0123456789abcdef'

    #create iv
    # iv must >= 16
    iv = Random.new().read(AES.block_size)
    #iv = b'0' * 16
    
    #dicotionary data set
    cookie = {}
    cookie['password'] = 'pass1'
    cookie['username'] = 'user1'
    cookie['admin'] = 0

    print("cookie")
    print(cookie)

    #dump to json
    cookie_data = json.dumps(cookie, sort_keys=True)

    #aes create
    aes = AES.new(key, AES.MODE_CBC, iv)
    raw = pad(cookie_data)

    #encrypt
    encrypted =  aes.encrypt(raw.encode('ascii'))

    #encode to base64
    encoded64 = base64.b64encode(iv + encrypted)
    str_encoded64 = encoded64.decode('ascii')

    print("encoded64")
    print(str_encoded64)

###　encrypt encode ,OK

    str_encoded64 = mod_adminflg(str_encoded64)
### next decode /decrypt
    #decode from base64
    dec_encrypted = base64.b64decode(str_encoded64)

    #pickout iv
    dec_iv = dec_encrypted[:16]

    #aes create
    aes = AES.new(key, AES.MODE_CBC, dec_iv)

    #decrypt
    dec_decripted = aes.decrypt(dec_encrypted[16:])
    dec_unpad = unpad(dec_decripted)
    #load json
    dec_jsondata = json.loads(dec_unpad)

    print("dec_jsondata")
    print(dec_jsondata)
    #pickout admin flag
    flgAdmin = dec_jsondata["admin"]
    print("flgAdmin")
    print(flgAdmin)

# last little more
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
