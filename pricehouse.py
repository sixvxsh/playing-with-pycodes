# -*- coding: utf-8 -*-
"""
Created on Fri May 27 15:50:59 2022

@author: s
"""

price_of_house = 1000000
good_credit = True


if good_credit:
    down_payment = 0.1 * price_of_house
else:
    down_payment = 0.2 * price_of_house
    
print(f"down_payment: ${down_payment}")