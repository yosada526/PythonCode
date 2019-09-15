#!/usr/bin/env python3
# coding: utf-8
"""python script
"""

import Crypto.Cipher.AES as AES


def main():
    """main
    """
    key = b'0123456789abcdef'
    iv = b'0' * 16

    iv2 = bytes(iv[:16])
    # AES-CBC モードで暗号化
    #aes = AES.new(key, AES.MODE_CBC, iv)
    aes = AES.new(key, AES.MODE_CBC, iv2)
    # bytes 型を渡す
    cipher = aes.encrypt('python script000'.encode('ascii'))
    # 使い回せないでのデコード用を新しく用意する
    aes = AES.new(key, AES.MODE_CBC, iv)
    # bytes 型が返る
    plain = aes.decrypt(cipher).decode('ascii')
    print(plain)


if __name__ == '__main__':
    main()
