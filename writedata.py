# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 20:21:06 2022

@author: s
"""

file_name = 'mydata3.txt'
with open (file_name, 'a') as file:
    for i in range(10):
        file.write("\nit's test")
