#!/usr/bin/python2
# -*- coding: utf-8 -*-

import functions as func
import time
import os

def williams():
	print "Do you want manualy enter settings? (y/n)"
	manual = str(raw_input("$ "))
	if manual == "n":
		p, q = func.rand34()
		n = p*q
		print "[ Williams ] p =",p,"q =",q
		print "[ Williams ] n =",n
		
	elif manual == "y":
		p = int(raw_input("p = "))
		q = int(raw_input("q = "))
		n = p*q
		print "[ Williams ] n =",n
		s = int(raw_input("s = "))
		k = 0.5*( 0.25*(p-1)*(q-1)+1 )
		print "[ Williams ] k =", k

	print "[ Williams ] Type 'encode'/'decode', or 'exit'"
	method = str(raw_input("$ "))

	while len(method)>1:
		if method == "exit":
			os._exit(1)
		if method == "encode":
			text = str(raw_input("input text [encode] $ "))
			start_time = time.time()
			size = len(text)
			print "[ Williams ] text length:",size

			text_int = []

			i = 0

			while i < size:
				text_int.append(ord(text[i]))
				i = i+1

			text_crypt = []
			text_M_one = []
			text_C2    = []
			i = 0
			while i < size:
				text_M_one.append(int((s ** C1)*text_int[i] % n))
				text_crypt.append(int(text_int[i]*text_int[i] % n))
				i = i+1

			print "[ Williams ] Encrypted:",text_crypt
			print "[ Williams ] Time elapsed:",time.time()-start_time

		if method == "decode":
			text = [eval(i) for i in raw_input('input text [decode] $ ').split()]
			print text

			start_time = time.time()
			size = len(text)
			print "[ Williams ] text length:",size

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
				m_p = text[i] ** (1/4 * (p+1)) % p
				m_q = text[i] ** (1/4 * (q+1)) % q

				r  = (y_p*p*m_q + y_q*q*m_p) % n
				r1 = n-r
				s  = (y_p*p*m_q - y_q*q*m_p) % n
				s2 = n-s


				text_decrypt_a.append(chr(int(r)))
				text_decrypt_b.append(chr(int(r1)))
				text_decrypt_c.append(chr(int(s)))
				text_decrypt_d.append(chr(int(s2)))
				i = i+1

			print "[ Williams ] Probably variants:"
			print "[ Williams ] A:"
			print_text(text_decrypt_a)
			print "[ Williams ] B:"
			print_text(text_decrypt_b)
			print "[ Williams ] C:"
			print_text(text_decrypt_c)
			print "[ Williams ] D:"
			print_text(text_decrypt_d)
			print "Time elapsed:",time.time()-start_time
		print "[ Williams ] Type 'encode'/'decode' for continue, or 'exit'"
		method = str(raw_input("$ "))

def print_text(text):
	print "[",

	i = 0
	while i<len(text):
		print "{}".format(text[i]),
		i = i+1
		if i!=len(text):
			print ",",
	print "]"

