# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 15:10:51 2022

@author: s
"""

import json

file_name = 'password.json'
with open(file_name) as file:
    password = json.load(file)
    print(f'your password was {password}')