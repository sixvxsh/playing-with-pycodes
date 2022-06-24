# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 17:58:13 2022

@author: s
"""


num = int(input())
    
yekan = num % 10
sadgan = num // 100
komak_dahgan = num // 10
dahgan = komak_dahgan % 10
new_num = str(yekan) + str(dahgan) + str(sadgan)

print(2*int(new_num))
