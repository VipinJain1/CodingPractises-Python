# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 20:51:35 2021

@author: VIP
"""

def addDigits( n: int) -> int:
       if n <=9:
           return n
       sm =0  
       while (True):
           while (n):
               sm = sm + int (n%10)
               n = n//10
           if sm <=9:
               return sm
           else:
               n = sm
               sm  =0


n =38

print (addDigits(n))