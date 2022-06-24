# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 16:34:39 2022

@author: s
"""

def shomaresh(a):
    if a <= 0:
     print('payan')
    else:
     print(a)
     shomaresh(a-1)
     
     
def chap_ebarat(ebarat , a):
    if a <= 0:
        return
    print(ebarat)
    chap_ebarat(ebarat, a-1)
    