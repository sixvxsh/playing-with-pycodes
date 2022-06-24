# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 16:59:54 2022

@author: s
"""

class Shomaresh:
    def __init__(self , v: int=0 , i: int=1 ) -> None:
        self.val = v
        self.incr = i
    
    def __repr__(self) -> str:
        return str(self.val)

    def afzayesh(self) -> None:
        self.val += self.incr



