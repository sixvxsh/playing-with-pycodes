# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 03:06:39 2021

@author: s
"""


w = input('write a thing :   ')
v = ['a', 'i', 'o', 'e', 'u']
found = {}

for letter in w:
    if letter in v:
        found.setdefault(letter , 0)
        found[letter] += 1
for k, v  in found.items():
    print(k, 'was found' , v , 'time(s).')
        
