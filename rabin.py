#!/usr/bin/python2
# -*- coding: utf-8 -*-

import functions as func
import time
import os

## INPUT
# rabin(TEXT, METHOD,p,q)

def rabin(input, method, p, q):
    n = p*q
    text = input
    # encode - 1
    if method == 1:
        start_time = time.time()
        size = len(text)
        print "[ Rabin ] text length:",size

        text_int = []

        i = 0

        while i < size:
            text_int.append(ord(text[i]))
            i = i+1

        text_crypt = []
        i = 0
        while i < size:
            text_crypt.append(int(text_int[i]*text_int[i] % n))
            i = i+1

        print "[ Rabin ] Encrypted:",text_crypt
        finish_time = time.time()-start_time
        print "[ Rabin ] Time elapsed:",finish_time
        text_crypt = ' '.join([str(i) for i in text_crypt]) 
        return [finish_time, text_crypt]

    if method == 0:
        text = text.split(' ')
        print text

        start_time = time.time()
        size = len(text)
        print "[ Rabin ] text length:",size

        text_decrypt_a = []
        text_decrypt_b = []
        text_decrypt_c = []
        text_decrypt_d = []

        tmp = []
        tmp = func.egcd(p,q)
        y_p = tmp[1]
        y_q = tmp[2]

        i = 0
        while i < size:
            m_p = int(text[i]) ** (1/4 * (p+1)) % p
            m_q = int(text[i]) ** (1/4 * (q+1)) % q

            r  = (y_p*p*m_q + y_q*q*m_p) % n
            r1 = n-r
            s  = (y_p*p*m_q - y_q*q*m_p) % n
            s2 = n-s


            text_decrypt_a.append(chr(int(r)))
            text_decrypt_b.append(chr(int(r1)))
            text_decrypt_c.append(chr(int(s)))
            text_decrypt_d.append(chr(int(s2)))
            i = i+1

        print "[ Rabin ] Probably variants:"
        print "[ Rabin ] A:"
        print_text(text_decrypt_a)
        print "[ Rabin ] B:"
        print_text(text_decrypt_b)
        print "[ Rabin ] C:"
        print_text(text_decrypt_c)
        print "[ Rabin ] D:"
        print_text(text_decrypt_d)
        finish_time = time.time()-start_time
        print "Time elapsed:",finish_time
        text_decrypt_a = ''.join([str(i) for i in text_decrypt_a])
        text_decrypt_b = ''.join([str(i) for i in text_decrypt_b])
        text_decrypt_c = ''.join([str(i) for i in text_decrypt_c])
        text_decrypt_d = ''.join([str(i) for i in text_decrypt_d])
        
        print_text(text_decrypt_a)
        print_text(text_decrypt_b)
        print_text(text_decrypt_c)
        print_text(text_decrypt_d)
        return [finish_time,text_decrypt_a,text_decrypt_b,text_decrypt_c,text_decrypt_d]


def print_text(text):
	print "[",

	i = 0
	while i<len(text):
		print "{}".format(text[i]),
		i = i+1
		if i!=len(text):
			print ",",
	print "]"

