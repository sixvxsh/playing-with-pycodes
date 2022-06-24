# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 02:30:24 2022

@author: s
"""

w = input (' write a thing :')
v = set('aeiou')
found = v.intersection(set(w))

for i in found:
    print(i)
 
