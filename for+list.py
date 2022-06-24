# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 15:05:42 2021

@author: s
"""

Q = ['i' , 'u' , 'o' , 'e' , 'a']
p = 'sardasht'
found = []

for letter in p:
    if letter in Q:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)
    