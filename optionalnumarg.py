# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 19:01:12 2022

@author: s
"""

def func1(*args):
    for arg in args:
        print(arg)
    
    
def miangin(aval , *baghi):
    return (aval + sum(baghi)) /(1 + len(baghi))


def func2(**kwargs):
    for k, v in kwargs.items():
        print ('%s == %s' %(k , v))


def func3(arg1 , arg2 , arg3):
    print ('arg1' , arg1)
    print ('arg2' , arg2)
    print ('arg3' , arg3)