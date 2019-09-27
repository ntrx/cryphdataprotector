#!/usr/bin/python2
# -*- coding: utf-8 -*-

import functions as func
import time
import os
## INPUT:
# rsa (text, [enc/dec - 1/0],[enc/dec settings 1 - manual, 0 - auto], p, q)
# 1: text - input text (letters)
# 2: method - number '1' if encode
#         - number '0' if decode
# 3 4 5:- parametres p and q, e.

## OUTPUT:
# 1: array of int numbers



        
def rsa(text,method,p,q,e):
    n = p*q
    key = (p-1)*(q-1)
    tmp = func.egcd(e,key)
    d = int(tmp[1])
       

    # encode  = 1 
    if method == 1:
        start_time = time.time()
        size = len(text)
        print "[ RSA ] text lenght:", size
        
        text_int = []
        i = 0
        while i < size:
            text_int.append(ord(text[i]))
            i = i+1
        
        text_crypt = []
        i = 0
        while i < size:
            text_crypt.append(int(text_int[i] ** e % n))
            i = i+1
        
        print "[ RSA ] Encrypted:", text_crypt
        finish_time = time.time()-start_time

        text_crypt = ' '.join([str(i) for i in text_crypt])        
        print "[ RSA ] Time elapsed:",finish_time, "ms"
        return [finish_time,text_crypt]
        
    # decode = 0
    if method == 0:
        print text
        text = text.split(' ')

        
        
        size = len(text)
        print "[ RSA ] text length:",size
        text_decrypt = []
        start_time = time.time()
        i = 0
        while i < size:
            text_decrypt.append(chr(int(int(text[i]) ** d % n)))
            i = i+1
        print "[ RSA ] Decrypted:",text_decrypt
        finish_time = time.time()-start_time
        print "[ RSA ] Time elapsed:",finish_time, "ms"
        text_decrypt = ''.join([str(i) for i in text_decrypt])
        return [finish_time,text_decrypt]

        