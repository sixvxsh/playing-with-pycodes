# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 06:07:08 2021

@author: s
"""
phrase = '!Salam va vaght bekheyr !'
ph_list = list(phrase)
print(phrase)
print(ph_list)
for i in range(2):
    ph_list.pop()
ph_list.pop(0)


ph_list.remove('v')
ph_list.remove(' ')

ph_list.insert(2 , ph_list.pop(15))
ph_list.insert(3, ph_list.pop(16))
ph_list.insert(4, ph_list.pop(13))
ph_list.insert(5, ph_list.pop(6))
ph_list.insert(6, ph_list.pop(19))


for i in range(13):
    ph_list.pop()
new_phrase = ''.join(ph_list)
print(ph_list)
print(new_phrase)