# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 13:31:18 2021

@author: VIP
"""


def viralAdvertising(n):
    # Write your code here
    
   start =2
   count  =1
   liked =2
   
   while (count <=n):
       liked = int (liked*3)
       liked = int (liked/2)
       count = count  +1 
       print (liked)
    
   return liked 

n=5
print (viralAdvertising(n))
    