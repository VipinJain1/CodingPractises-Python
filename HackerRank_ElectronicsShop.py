# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 15:01:11 2021

@author: VIP
"""

b =5

keyboards= [4]
drives= [5]

dist =b
myTotal =b
possible = -1
for i in  range (0,len (keyboards)):
    for j in range (0,len (drives)):
        
        totalPrice = keyboards[i] + drives[j]
        if (totalPrice <=b):
            possible =1
            if ((b - totalPrice)< dist  and  (b - totalPrice) >=0):
                myTotal =totalPrice
                dist = b - totalPrice
if (possible ==1):
    print (myTotal)
else:
    print (-1)       