#!/usr/bin/python2
# -*- coding: utf-8 -*-

import functions as func
import random
import time
import os

## INPUT elgamal(TEXT,METHOD,p,g,k,x)

def elgamal(input,method,p,g,k,x):
    text = input
    y = g ** x % p
    a = g ** k % p
    # 1 - encode
    if method == 1:
        start_time = time.time()
        size = len(text)
        print "[ Elgamal ] Text length:",size

        text_int     = []
        text_crypt   = []
        i = 0

        while i < size:
            text_int.append(ord(text[i]))
            i = i+1

        i = 0
        while i < size:
            text_crypt.append((y ** k)*text_int[i] % p)
            i = i+1
        finish_time = time.time()-start_time
        print "[ Elgamal ] Encrypted:",text_crypt
        print "[ Elgamal ] Time elapsed:",finish_time,"ms"
        text_crypt = ' '.join([str(i) for i in text_crypt]) 
        return [finish_time, text_crypt]
                
        
    if method == 0:
        text = text.split(' ')


        start_time = time.time()
        size = len(text)
        print "[ Elgamal ] text length:",size

        text_decrypt = []
        i = 0
        while i < size:
            text_decrypt.append(chr(int(text[i])*(a ** (p-1-x)) % p))
            i = i+1

        finish_time = time.time()-start_time
        print "[ Elgamal ] Time elapsed:",finish_time
        
        print "[ Elgamal ] Decrypted:", text_decrypt
        text_decrypt = ''.join([str(i) for i in text_decrypt])
        return [finish_time,text_decrypt]
