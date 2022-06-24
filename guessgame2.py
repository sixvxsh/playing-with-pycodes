# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 16:19:50 2022

@author: s
"""



import random

guess_pc = random.randint(1 , 99)
print(guess_pc)
 
my_numb_is_smaller = 's'
my_numb_is_bigger = 'b'
equal = 'e'

mymind = input('tell a thing to computer: ')

while mymind != 'e':
    
    
    if mymind == 's':
        guess_pc1 = random.randint( 1 , guess_pc ) 
        print(guess_pc1)
    if mymind == 'b':
        guess_pc2 = random.randint( guess_pc , 99)
        print(guess_pc2)
    mymind = input('tell a thing to computer: ')


print('we win')


    

    




    
    

