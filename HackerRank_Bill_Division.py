# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 22:27:14 2021

@author: VIP
"""


def bonAppetit(bill, k, b):
    # Write your code here
    
    if sum(bill)  ==0:
        return 0
    
    billtoPay = int (b - (sum (bill) -  bill[k])/2)
    
    if billtoPay <=0:
        print ("Bon Appetit")
    else:
        print (billtoPay)    
    
    
    
bill =[3,10,2,9]
#bill = [2,0,0,0]
k =1
b =7

bonAppetit(bill,k,b)