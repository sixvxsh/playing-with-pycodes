# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 10:53:33 2022

@author: s
"""


print('give two number for division')
print('with q you can quit the program')

while True:
    adad_aval = input('\nadad_aval: ')
    if adad_aval == 'q':
        break
    adad_dovom = input('\nadad dovom: ')
    if adad_dovom == 'q':
        break
    try:  
        hasel_taghsim = int(adad_aval) / int(adad_dovom)
    except ZeroDivisionError:
        print('taghsim bar zer0 emkan pazir nist')
    else:    
        print(hasel_taghsim)
    