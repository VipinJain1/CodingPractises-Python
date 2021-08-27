# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 19:10:44 2021

@author: VIP
"""

def plusOne(digits):
    strings = [str(integer) for integer in digits]
       a_string = "".join(strings)
       an_integer = int(a_string) +1
       return [int (i) for i in str(an_integer)]
           
       

digits = [9,9]
print (plusOne(digits))
