# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 17:32:38 2021

@author: VIP
"""
def rotLeft(a, d):
    
    for i  in range (1,d+1):
      atemp = a[0]
      a = a[1:]
      a.append(atemp)
    return a

        
    
    



d = 4
a = [1,2,3,4,5]
print (rotLeft(a, d))

       