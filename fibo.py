# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 18:41:40 2022

@author: s
"""

def fibonacci(n: int) ->int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
    