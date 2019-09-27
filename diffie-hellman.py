#!/usr/bin/python2
# -*- coding: utf-8 -*-

import functions as func
import time
import os


def dh():
	d = -1
	print "Do you want manualy enter settings? (y/n)"
	manual = str(raw_input("$ "))
	if manual == "n":
		while d<0:
			p = func.random_n(10,100)
			q = func.random_n(10,100)

			while len(str(p)) != len(str(q)):
				q = func.random_n(10,100)

			while p == q:
				q = func.random_n(10,100)

			n = p*q
			key = (p-1)*(q-1)
			e = func.random_n(0,10)
			while func.gcd(key,e) != 1:
				print "[ DH ] e generation failure, trying another e..."
				e = func.random_n(0,10)
			tmp = func.egcd(e,key)
			d = int(tmp[1])
		print "[ DH ] p =",p,"q =",q
		print "[ DH ] n =",n
		print "[ DH ] e =",e,"key =",key
		print "[ DH ] d =",d
	elif manual == "y":
		p = int(input("p = "))
		q = int(input("q = "))
		n = p*q
		key = (p-1)*(q-1)
		e = int(input("e = "))
		tmp = func.egcd(e,key)
		d = int(tmp[1])

	print "[ DH ] Choose 'encode' or 'decode' for proceed, or exit for quit"
	method = str(raw_input("$ "))
	while len(method) > 1:
		if method == "exit":
			os._exit(1)
		if method == "encode":
			text = str(raw_input("input text [encode] $ "))
			start_time = time.time()
			size = len(text)
			print "[ DH ] text lenght:", size

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

			print "[ DH ] Encrypted:",text_crypt
			print "[ DH ] Time elapsed:",time.time()-start_time, "ms"
		if method == "decode":
			text = [eval(i) for i in raw_input('input text [decode] $ ').split()]
			print text
			start_time = time.time()
			size = len(text)
			print "[ DH ] text length:",size

			text_decrypt = []
			i = 0
			while i < size:
				text_decrypt.append(chr(int(text[i] ** d % n)))
				i = i+1
			print "[ DH ] Decrypted:",text_decrypt
			print "[ DH ] Time elapsed:",time.time()-start_time, "ms"
		print "[ DH ] Type encode/decode to continue or 'exit' for exit"
		method = str(raw_input("$ "))

