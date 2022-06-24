# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 13:33:46 2022

@author: s
"""

w = input('write a thing :   ')
v = {'a', 'i', 'o', 'e', 'u'}
#or v= set('aeiou')

found = v.difference(set(w))
for vowel in found:
    print(vowel)

