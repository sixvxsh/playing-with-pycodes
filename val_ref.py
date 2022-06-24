# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 12:56:26 2022

@author: s
"""

def dobarabar(arg):
    print('before : ' , arg)
    arg = arg * 2
    print ('after : ' , arg)
    
def change(arg):
    print('before : ' , arg)
    arg.append('abcd')
    print('after :' , arg)