# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 22:27:14 2021

@author: VIP
"""

def bonAppetit(bill, k, b):
    # Write your code here
    
    total  = round (abs(sum (bill) - bill[1])/2)
    x = int (b - total)
    if x ==0:
        print ('Bon Appetit')
    else:
        print (int (b - total))


bill =[3,10,2,9]
k =1
b =12

bonAppetit(bill,k,b)