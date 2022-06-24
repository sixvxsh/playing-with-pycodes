# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 23:54:21 2022

@author: s
"""


import json 

file_name = 'mypassword.json'
try:
    with open (file_name) as file:
        password = json.load(file)
except FileNotFoundError:
    password = input('Enter your password: ')
    with open (file_name , 'w') as file:
        json.dump(password , file)
        print(f'your password is {password}')
    
else:
    print('your password was' , password)
            
        
