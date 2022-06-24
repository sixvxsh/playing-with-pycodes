# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 16:39:48 2022

@author: s
"""
# file_name = 'mydata.txt'
# with open (file_name) as file:
#     for line in file:
#         print(line)
        
        
file_name = 'mydata.txt'
with open(file_name) as file:
    lines = file.readlines()
    print(lines)
    
