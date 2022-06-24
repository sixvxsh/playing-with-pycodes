# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 15:22:23 2022

@author: s
"""


class Zaman:
    """
    Nemayeshe zamane rooz.
    
    att : Hour , min , Secnod 
    
    """
    
zaman = Zaman()
zaman.hour = 8
zaman.minute = 45 
zaman.second = 12


def print_zaman(t):
    """
    Nemayeshe string az zaman 
    t = Zaman Object 
    
    """
    print('(%.2d:%.2d:%.2d)' %(t.hour , t.minute , t.second))
    
    
#pure_functin
def add_time(t1 , t2):
#    majmoo = Zaman()
#    majmoo.hour = t1.hour + t2.hour
#    majmoo.minute = t1.minute + t2.minute
#    majmoo.second = t1.second +t2.second
    
# if majmoo.second >= 60:
#     majmoo.second -= 60
#        majmoo.minute += 1
        
#    if  majmoo.minute >= 60:
#         majmoo.minute -= 60
#        majmoo.hour += 1
#    return majmoo

    if not zaman_sahih(t1) or zaman_sahih(t2):
        raise ValueError('Object zaman sahih nist')
    seconds = zaman_be_int(t1) + zaman_be_int(t2)
    return int_be_zaman(seconds)



#modifier_function_of_add_time
def afzayesh(zaman , seconds):
    """ yek obj zaman az class migirad va
    be att haye an seconds ra ezafe mikonad
    """
    zaman.second += seconds
    
    if zaman.second >= 60:
        zaman.second -= 60
        zaman.minute += 1
        
    if  zaman.minute >= 60:
         zaman.minute -= 60
         zaman.hour += 1
         
#purefunction      
def zaman_be_int(zaman):
    """ tabdil koll type haye zamani be sanie """
    
    minutes = zaman.hour * 60 + zaman.minute
    seconds = minutes * 60 + zaman.second
    return seconds
    

def int_be_zaman(seconds):
    zaman = Zaman()
    minutes , zaman.second = divmod(seconds , 60)
    zaman.hour , zaman.minute = divmod(minutes , 60)
    return zaman

def zaman_sahih(zaman):
    if zaman.hour < 0 or zaman.minute < 0 or zaman.second < 0:
        return False
    if zaman.minute >= 60 or zaman.second >= 60:
        return False
    return True
    
    
     
    
          