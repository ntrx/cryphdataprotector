#!/usr/bin/python2
# -*- coding: utf-8 -*-

import random
import math

def is_prime(n):
        if n <= 1:
                return 0
        elif n <= 3:
                return 1
        elif (n % 2 == 0) or (n % 3 == 0):
                return 0

        i = 5
        while (i <= math.sqrt(n)):
                if (n % i == 0) or (n % (i+2) == 0):
                        return 0
                i = i+6
        return 1

def random_n(len_from, len_to):
        len_from = len_from * 10
        len_to   = len_to *10

        n = random.randint(len_from, len_to)
        while True:
                if is_prime(n) == 1:
                        return n
                n = random.randint(len_from, len_to)

def gcd(a, b):
        if b == 0:
                return a
        else:
                return gcd(b, a % b)

def egcd(a, b):
        if b == 0:
                return (a, 1, 0)
        else:
                d, x, y = egcd(b, a % b)
                d, x, y = d, y, x - (a//b)*y
                return (d, x, y)

def rand34():
        len_from = 3
        len_to   = 100
        step     = 4

        list = []
        items = 0

        for i in range(len_from,len_to,step):
                if is_prime(i) == 1:
                        list.append(i)
                        items = items+1

        n = random.randint(len_from, items-1)
        return (list[n], list[n-1])

def even(n):
        if n % 2 == 0:
                return 1
        return 0

def j(s, n):
        r = 1
        while s != 0:
                #rint s
                while even(s) == 1:
                        print s
                        s = s // 2
                        if (n % 8 == 3) or (n % 4 == 3):
                                r = -r
                tmp = s
                s = n
                n = tmp
                if (s % 4 == 3) and (n % 4 == 3):
                        r = -r
                        s = s % n
                if n == 1:
                        return r
                return 0
        
                
                
                
