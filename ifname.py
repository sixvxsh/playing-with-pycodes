# -*- coding: utf-8 -*-
"""
Created on Fri May 27 19:23:05 2022

@author: s
"""

name = input("what's your name: ")

if len(name) < 3:
    print("Error: Name must be at least 3 characters")
    name = input("what's your name: ")
elif len(name) > 50:
    print("Error: Name can be a maximum of 50 characters")
    name = input("what's your name: ")
else:
    print("name is fine ")
    password = input("what's your password:  ")