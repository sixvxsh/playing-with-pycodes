# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 14:58:09 2022

@author: s
"""


import json

try:
    file_name = 'password.json'
    with open(file_name) as file:
        numbers = json.load(file)
except FileNotFoundError:  
    print("this file hasn't exist")
else:
    print(f'your password was {numbers}')