# -*- coding: utf-8 -*-
"""
Created on Fri May 27 19:49:38 2022

@author: s
"""

weight = int(input("weight: "))
unit = input('(L)bs or (K)g:')

if unit.upper() == "L":
    converted = weight * 0.45
    print(f"you are {converted} kilos")

else:
    converted = weight / 0.45
    print(f"you are {converted} pounds")
    
        
