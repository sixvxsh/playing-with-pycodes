# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 13:31:52 2022

@author: s
"""


def shomaresh_tedad_arg(file_name):
    try: 
        with open(file_name) as file:
            content = file.read()
    except FileNotFoundError:
            print("this file is not exist")
            # pass
    else:
         arg = content.split()
         tedad_arg = len(arg)
         print(f'this file {file_name} has {tedad_arg} arg')
         
file_name = ['mydata.txt','mydatax','mydata2.txt','mydata3.txt','mydata4']
for file in file_name:
    shomaresh_tedad_arg(file)
