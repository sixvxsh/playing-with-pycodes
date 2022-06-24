# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 14:40:10 2022

@author: s
"""


import json

numbers = [100 , 200 , 350 , 450]

file_name = 'numbers.json'
with open(file_name , 'w') as file:
    json.dump(numbers , file)