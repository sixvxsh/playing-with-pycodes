# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 15:07:20 2022

@author: s
"""

import json 

password = input('Enter your password: ')
file_name = 'password.json'
with open(file_name , 'w') as file:
    json.dump(password , file)
    print(f'your password is {password}')