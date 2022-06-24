# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 13:07:43 2022

@author: s
"""


file_name = 'mydata.txt'
try: 
    with open(file_name) as file:
        content = file.read()
except FileNotFoundError:
        print("this file is not exist")
else:
     arg = content.split()
     tedad_arg = len(arg)
     print(f'this file {file_name} has {tedad_arg} arg')
