# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 15:57:57 2022

@author: s
"""


import random

javab_pc = random.randint(1 , 99)

name = input('what is your name: ')
guess = int(input('what is your guess: ' ))

while javab_pc != guess:
    if guess > javab_pc:
        print('mine is smaller')
    else:
        print('mine is larger')
    guess = int(input('give a number: ')) 
     
print('woooow' , name , 'you win my darling')


