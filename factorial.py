# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 17:05:51 2022

@author: s
"""


def factorial(n: int) -> int:
    if not isinstance(n, int):
        print('faghat int bede')
        return None
    elif n < 0:
        print('factorial baraye adad manfi tarif nemishavad')
        return None
    elif n == 0:
        return 1
    else:
        return n * (n-1)