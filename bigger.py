# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 17:01:26 2022

@author: s
"""

A = int (input())
B = int (input())


if A == B:
    print(A)
if  A < 0 or B < 0:
    print ('Error')
elif A > B:
    print(A)
else:
    print (B)
    
