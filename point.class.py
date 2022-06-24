# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 17:00:43 2022

@author: s
"""

class Point:
    """ nemayesh yek noghte dar 2D. """
     
def print_point(p):
    print ('(%g , %g)' %(p.x , p.y))
    
    
class Mostatil:
    """ nemayesh mostatil 
    
    Attributes : arz , ertefa , gushe"""
    
mos1 = Mostatil()
mos1.arz = 50.0
mos1.ertefa = 80.0
mos1.gushe = Point()
mos1.gushe.x = 0.0  
mos1.gushe.y = 0.0

    
def markaz(most):
    p = Point()
    p.x = most.gushe.x + most.arz/2
    p.y = most.gushe.y - most.ertefa/2
    return p
    
mos1.arz += 500
mos1.ertefa += 100

def taghir_andaze_mostatil(most , tarz , tertefa):
    most.arz += tarz
    most.ertefa += tertefa
    
    

    