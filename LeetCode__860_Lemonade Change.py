# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 13:34:00 2021

@author: VIP
"""

def lemonadeChange(bills):
    ln = len(bills)
    if ln ==0:
        return False
    
    if bills[0] !=5:
        return False
    cash = {}
    cash[5] =1
    cash[10] =0
    cash[20] =0
    
    for i in range (1, ln):
        
        if bills[i] ==5:
            if 5 in cash.keys():
                cash[5] +=1
            else:
                cash[5] =1
            stillGood = True
        elif bills[i] ==10:
            if cash[5] >=1:
                cash[5] -=1
                if 10 in cash.keys():
                    cash[10] +=1
                else:
                    cash[10] =1
                stillGood = True
            else:
                stillGood = False
                return False
                
                
        elif bills[i]  ==20:
            if cash[10] >=1 and cash[5] >=1:
                cash[5] -=1
                cash[10] -=1
                stillGood = True
            elif cash[5] >=3:
                cash [5] = cash[5]-3
                stillGood = True
            else:
                stillGood = False
                return False

        
    if stillGood ==True:
        return True
    else:
        return False

bills = [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,20,5,20,5,5,5,10,20,5,5,10,5,10,5,10,5,5,5,20,10,5,5,5,5,5,5,20,5,10,10,20,5,20,5,5,10,5,20,5,5,5,10,5,10,10,10,10,10,5,20,5,20,20,5,5,5,5,5,5,5,20,10,5,5,5,20,5,5,5,20,5,5,5,5,20,20,5,5,20,20,5,5,5,20,5,5,10,10,10,5,20,20,5,20,5,5,10,10,20,20,5,5,20,10,5,5,10,20,5,20,5,5,5,20,5,20,5,5,5,5,5,5,5,20,20,10,5,5,5,5,20,5,20,20,5,10,10,20,20,20,5,5,5,5,10,10,5,5,20,20,10,5,5,10,20,5,5,5,5,5,20,10,20,5,5,5,10,5,5,5,10,5,5,10,10,20,5,5,10,10,10,10,5,5,5,5,20,10,5,20,10,5,5,5,20,10,5,5,5,5,5,5,5,10,10,10,5,20,5,5,5,5,20,5,10,10,20,5,5,5,5,10,5,5,5,10,10,5,5,5,5,5,10,5,5,10,20,20,5,10,5,5,5,10,5,5,5,20,5,5,5,20,5,5,5,5,5,10,10,5,5,5,5,5,10,10,5,5,5,20,5,5,5,5,5,5,5,5,10,5,10,5,20,5,20,20,5,20,5,10,20,5,5,5,5,5,5,5,10,5,20,5,10,5,10,5,5,5,5,20,10,5,20,10,5,10,5,5,20,10,20,10,5,5,5,5,5,5,20,5,10,10,20,5,5,10,5,5,5,5,20,20,5,10,5,5,20,5,10,5,20,5,5,5,20,5,5,5,10,5,10,20,20,10,5,20,20,10,10,20,5,20,5,5,10,5,5,10,5,5,20,5,5,5,5,5,5,5,5,5,5,20,5,5,5,20,5,10,5,10,10,20,5,5,5,20,5,5,20,5,20,5,5,5,10,5,5,10,20,5,5,10,10,5,5,5,20,20,20,5,5,5,20,10,20,20,10,5,5,5,5,10,5,5,5,5,5,10,5,5,5,5,5,5,5,20,5,5,10,20,5,5,5,5,10,5,5,5,20,5,5,20,20,10,20,10,5,5,5,5,20,20,10,10,20,20,5,5,5,5,5,5,5,5,10,5,5,20,5,5,5,20,5,5,10,10,5,5,5,5,10,5,5,5,5,10,5,10,5,20,5,5,5,10,5,20,5,20,5,5,5,5,10,5,20,5,10,5,5,5,10,5,10,10,5,5,10,20,5,5,5,10,5,5,5,5,10,10,5,10,10,20,5,10,5,5,5,5,5,10,20,20,5,5,5,5,10,10,5,20,5,5,10,5,20,5,5,5,5,5,10,10,5,5,5,5,10,5,5,20,5,5,5,5,5,5,20,5,5,10,5,5,5,10,5,5,5,5,20,5,5,20,10,20,20,20,5,10,5,5,5,5,20,5,5,10,10,10,5,5,20,5,5,20,20,5,5,5,20,5,5,5,5,20,5,5,10,5,20,10,5,5,5,20,5,10,10,5,5,5,20,5,5,5,5,5,5,10,5,5,10,10,5,20,10,20,5,5,5,5,5,20,5,5,20,5,5,5,5,20,5,5,20,10,20,10,5,20,5,5,5,5,5,5,5,5,20,5,20,5,10,5,10,5,5,5,10,5,10,5,5,5,5,20,10,10,5,10,5,5,5,20,20,5,5,5,5,5,20,5,5,10,20,5,5,5,5,5,5,5,5,5,5,10,20,5,10,5,5,5,10,5,5,5,5,10,10,10,10,5,10,5,20,5,5,20,10,5,5,5,5,5,5,5,5,5,20,5,5,10,10,5,10,5,10,5,5,20,20,5,10,5,10,5,5,20,10,5,20,5,20,20,5,10,10,10,10,20,10,5,5,5,20,5,10,20,5,5,5,5,10,5,20,20,5,20,5,10,20,5,5,5,5,5,5,10,5,5,5,20,5,5,5,5,10,5,20,20,20,5,5,20,20,5,5,5,20,5,5,20,5,5,5,5,5,5,5,5,10,20,5,5,10,10,5,10,10,20,5,5,5,5,20,20,5,10,10,5,5,5,5,5,20,5,5,5,10,20,5,5,10,20,5,20,5,20,10,5,20,20,5,20,5,5,10,20,5,5,20,10,5,10,5,5,5,5,5,5,5,10,10,20,10,20,10,5,5,20,5,10,5,10,10,5,5,5,5,5,5,5,20,10,20,20,10,10,20,5,5,20,5,20,5,10,5,10,20,20,10,20,5,5,5,5,5,5,5,20,5,10,10,10,5,20,20,10,5,20,5,5,5,5,10,10,5,5,5,20,20,5,10,5,5,5,10,5,10,20,20,5,20,5,5,5,5,20,20,5,20,10,20,5,5,5,20,5,5,20,10,5,10,10,10,5,5,5,5,5,5,10,5,5,20,20,5,10,5,5,5,5,5,20,5,5,10,5,5,5,5,10,10,10,10,5,20,5,5,20,10,5,5,20,5,5,5,5,5,10,5,5,5,5,10,5,5,5,10,5,5,5,5,20,10,5,5,5,5,5,20,5,20,5,5,5,5,5,10,5,5,20,20,5,5,5,5,10,20,10,5,10,10,5,10,5,20,5,5,20,20,5,10,5,5,5,5,20,10,5,5,5,20,5,10,5,5,10,5,5,10,5,5,5,10,5,5,5,20,5,10,5,5,5,5,5,20,20,5,5,5,5,5,5,20,5,5,5,5,5,20,5,5,5,10,10,10,5,10,20,5,20,20,5,5,5,5,10,5,5,5,10,10,5,5,5,10,5,20,5,5,5,5,5,5,5,5,5,10,5,5,5,10,5,5,10,5,5,5,5,5,5,20,5,5,5,5,5,10,5,5,5,5,10,5,10,5,20,20,20,10,20,5,5,5,5,5,5,5,5,20,20,20,5,10,20,20,20,20,5,5,20,10,20,5,5,5,5,5,5,5,5,20,5,5,5,10,10,5,5,20,20,5,5,5,5,5,5,20,5,5,5,20,5,5,5,5,10,20,5,20,20,20,10,5,5,5,5,5,5,5,20,20,10,5,10,5,5,5,5,5,10,5,20,5,10,5,20,20,5,5,20,5,20,5,10,5,5,5,20,20,10,5,10,10,20,5,5,5,5,5,5,10,5,20,5,5,5,5,20,5,5,5,5,20,10,5,5,20,10,5,5,5,5,10,10,5,5,5,5,20,5,5,5,10,5,5,10,5,5,5,5,5,5,20,10,5,20,5,10,5,5,5,5,5,5,5,5,10,5,5,20,5,5,5,20,20,5,20,10,10,5,5,10,10,5,5,5,20,5,5,5,5,10,5,5,5,5,5,20,10,5,20,5,5,5,5,5,20,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,10,10,10,5,5,5,10,20,5,5,5,5,10,20,20,20,5,10,10,20,20,5,5,5,5,5,5,5,5,10,20,5,5,5,5,10,10,5,20,5,5,5,5,5,20,5,10,5,5,5,20,5,5,5,5,20,5,10,20,5,5,5,5,5,5,10,5,5,5,10,20,5,10,10,5,5,10,5,10,10,5,5,5,5,10,5,5,5,5,20,5,10,5,5,5,5,5,10,20,5,10,10,20,5,10,20,20,20,5,5,20,5,20,10,20,10,5,10,5,5,10,5,5,5,5,5,5,10,10,5,5,5,10,5,20,20,5,5,20,5,10,5,5,5,10,20,5,10,5,5,5,5,20,5,5,5,5,5,5,10,5,5,10,5,5,5,20,20,5,5,5,5,5,5,5,5,5,5,20,10,10,20,10,20,20,5,5,10,10,5,5,10,5,20,5,20,10,5,10,5,5,20,5,5,5,5,5,5,10,10,5,20,10,5,20,20,5,20,5,10,5,20,5,10,5,5,5,5,5,5,5,20,10,20,5,5,5,5,20,10,5,5,5,10,5,5,5,20,5,5,5,5,10,5,5,10,5,20,10,5,10,5,5,5,5,5,10,10,20,5,5,20,5,5,20,5,5,5,10,20,5,5,5,5,5,5,10,10,5,10,5,5,5,5,20,10,5,20,5,10,5,20,20,10,5,5,5,5,20,5,10,5,20,5,5,5,5,5,10,5,20,10,20,20,10,5,10,10,5,20,20,5,20,20,5,5,5,20,5,10,5,5,5,20,5,5,5,5,5,5,10,20,10,5,5,5,5,20,5,5,5,5,10,5,20,5,5,10,5,10,10,5,5,5,5,10,5,5,5,5,5,10,5,5,10,5,5,20,20,10,5,10,20,10,10,5,20,5,20,10,5,5,10,5,5,5,20,5,20,5,5,5,5,5,5,5,5,5,5,20,20,10,10,5,5,20,5,10,5,10,5,5,20,20,20,20,10,20,5,5,5,10,5,10,5,5,5,20,5,10,20,20,5,5,10,5,5,20,5,5,10,5,5,5,5,5,5,5,10,5,10,10,20,5,5,10,10,10,10,20,20,10,10,5,5,5,5,10,10,5,10,5,10,5,5,10,5,20,20,5,10,5,5,5,5,5,5,10,10,10,5,5,5,5,5,5,20,5,5,10,5,20,5,5,20,20,5,20,20,5,5,20,20,5,5,5,10,10,5,5,5,5,5,5,5,5,20,5,5,20,10,5,20,10,20,5,20,10,5,5,5,5,10,20,10,20,10,5,5,5,20,5,20,20,5,5,20,5,5,5,5,5,10,5,5,5,5,10,20,10,5,5,10,20,10,10,10,5,5,5,10,20,20,10,5,5,20,5,5,5,10,10,5,5,10,5,20,20,5,5,5,10,5,5,5,20,5,10,5,10,5,5,5,10,20,5,5,10,10,10,20,5,20,5,20,5,5,10,5,5,10,5,5,5,5,10,5,5,20,10,5,5,10,5,5,20,5,5,20,20,10,5,5,10,5,20,20,5,5,20,20,5,10,10,20,5,20,5,5,10,5,10,5,5,5,5,5,5,5,5,5,5,5,5,20,20,10,5,10,20,20,5,20,10,10,5,5,20,10,10,5,5,5,10,10,5,20,10,20,20,10,20,10,10,5,20,5,5,20,10,5,5,20,5,5,10,10,5,20,5,10,5,20,5,5,5,5,20,5,20,20,10,20,20,5,5,5,5,5,20,5,5,10,5,5,10,20,5,5,10,10,20,5,5,5,20,5,5,20,10,5,5,5,20,5,5,10,10,10,5,10,5,10,5,5,20,5,5,5,5,10,5,5,10,5,20,5,5,5,10,20,5,10,20,20,10,10,10,20,5,5,5,5,5,20,10,5,5,5,5,5,5,20,20,5,5,5,5,5,10,5,20,5,20,20,5,20,20,5,10,5,5,10,5,5,10,5,5,10,20,5,5,10,10,5,5,5,5,5,5,20,5,5,20,10,5,5,5,5,5,20,10,5,5,5,5,5,5,10,5,20,5,20,5,20,5,5,5,5,5,5,5,10,20,5,5,10,5,5,5,5,20,5,5,10,10,5,5,5,10,5,5,20,5,5,5,5,5,5,20,5,5,10,5,5,5,5,20,5,20,5,5,20,5,5,10,20,5,20,5,5,20,5,5,10,10,10,20,5,5,10,5,20,5,5,10,20,5,5,10,5,10,5,5,20,10,20,5,5,20,20,5,20,10,10,5,5,10,5,5,5,5,20,5,5,5,5,10,5,20,20,5,5,20,20,5,20,5,5,5,5,20,5,10,10,5,5,10,5,5,5,5,10,20,10,5,5,5,5,5,5,20,5,10,5,5,5,5,20,20,5,10,5,5,10,10,5,10,5,10,5,5,5,20,20,5,5,5,10,5,20,10,5,10,5,5,5,5,10,5,5,5,5,5,5,5,5,20,5,10,10,20,5,5,5,20,5,5,5,5,5,20,5,20,5,5,20,10,5,20,5,5,10,10,20,20,5,5,10,20,20,5,10,20,10,20,5,5,5,5,20,5,20,5,5,20,20,10,20,5,5,5,10,20,5,5,5,20,5,5,5,5,5,5,20,5,5,5,20,5,5,5,20,20,5,5,5,20,5,20,5,10,10,5,10,5,10,10,20,5,20,20,5,10,5,5,5,5,5,10,5,10,5,5,5,5,5,5,5,20,5,5,5,5,5,20,5,5,5,5,5,20,20,5,5,5,5,5,20,20,5,5,20,5,5,5,5,10,5,5,10,20,5,5,5,20,20,10,5,5,20,5,5,5,5,5,5,5,5,5,5,20,5,5,5,20,20,20,20,20,10,5,5,5,20,5,10,10,10,5,10,10,10,5,5,20,20,5,5,5,5,10,5,5,5,20,10,5,5,5,5,5,10,20,10,20,5,5,5,10,5,20,5,10,10,5,20,10,20,5,5,5,5,5,10,20,5,5,5,5,5,5,10,20,10,20,20,5,5,10,5,5,5,20,5,20,10,10,5,5,5,5,5,20,5,5,5,5,5,5,20,5,20,5,20,5,5,5,20,5,5,5,5,20,20,20,5,5,5,10,5,10,20,5,20,5,5,5,5,10,5,5,20,5,5,5,10,5,5,5,20,10,20,5,5,20,5,10,5,5,5,10,5,5,5,10,20,20,10,5,5,5,5,20,5,20,5,5,5,20,5,5,5,5,20,5,5,20,5,5,5,5,20,20,5,10,5,5,5,5,5,5,5,5,5,20,5,10,5,20,20,20,20,10,5,10,5,20,5,5,20,10,20,5,5,5,20,5,5,5,5,10,5,5,20,5,10,5,5,10,5,20,5,10,5,20,20,5,5,20,20,5,20,5,5,5,20,5,20,5,5,5,10,5,5,5,5,5,20,5,5,5,5,5,5,10,20,20,5,5,20,20,10,5,20,5,10,20,5,5,5,5,5,5,5,5,10,20,5,5,5,5,10,5,20,5,10,5,5,20,10,5,5,5,5,5,5,5,5,5,10,5,5,5,20,5,20,10,10,10,5,5,5,5,10,10,10,5,10,5,20,20,20,20,5,5,5,20,5,5,5,20,10,5,20,5,10,20,5,5,10,20,20,10,5,5,5,5,5,5,5,5,20,20,5,5,5,20,10,10,10,5,5,5,20,5,10,5,10,20,5,10,5,5,5,20,5,5,5,5,5,5,5,20,5,10,5,5,5,10,5,20,20,5,5,5,10,5,5,5,5,10,5,5,20,5,5,10,10,5,20,10,20,10,10,5,5,5,5,5,10,5,5,5,10,5,5,20,10,20,20,20,10,20,5,5,5,5,5,5,20,5,20,20,5,5,10,10,5,5,20,5,5,5,5,20,10,20,5,5,5,5,10,5,5,5,5,20,5,10,5,5,10,5,5,5,5,5,5,5,5,5,5,10,5,10,20,10,5,20,20,5,5,20,20,10,5,5,10,5,5,10,20,20,5,20,20,10,10,5,5,5,20,20,5,5,20,20,5,5,10,5,20,5,5,20,20,10,20,5,20,5,20,20,5,5,10,10,10,10,5,5,5,10,10,10,20,5,5,5,5,5,5,5,10,10,10,5,20,5,10,10,20,5,5,5,20,5,5,5,5,5,10,5,10,5,10,5,20,20,20,5,10,5,5,10,5,5,5,20,5,10,5,10,5,5,10,5,20,5,5,10,20,5,20,5,5,20,20,5,5,20,5,5,5,5,5,5,10,10,5,10,10,5,5,5,5,20,5,5,5,5,5,20,5,5,5,5,20,10,10,5,5,5,10,5,5,20,5,5,5,5,5,5,5,20,20,20,5,20,5,5,5,10,5,5,5,5,5,10,20,5,10,10,10,5,5,20,20,5,10,5,5,5,20,20,10,5,5,5,5,20,20,5,5,5,20,5,10,5,5,5,5,5,5,10,5,5,5,5,20,10,10,5,5,5,5,5,10,5,5,5,5,5,5,5,5,20,10,5,20,5,10,5,20,5,5,5,5,20,5,5,5,5,20,20,5,10,5,20,5,20,5,20,20,5,20,5,5,5,5,10,20,5,20,5,5,5,20,10,10,5,5,5,5,5,10,5,10,5,5,5,5,20,5,5,20,20,5,5,10,5,20,10,5,10,10,10,5,20,20,5,5,5,5,5,5,20,5,5,5,20,5,10,5,5,5,5,5,5,5,10,5,10,10,5,5,5,5,5,20,5,10,5,5,5,5,20,10,5,5,5,20,20,5,10,5,10,5,5,5,5,5,5,20,5,10,10,20,20,5,20,10,20,20,5,5,10,5,20,5,5,10,10,20,5,5,5,5,5,5,5,5,5,20,5,5,5,5,20,20,10,5,5,5,5,5,5,20,10,5,5,5,10,5,5,10,20,5,10,5,10,10,10,5,20,5,5,20,10,10,5,20,5,5,10,5,5,20,10,5,5,5,5,5,10,20,20,5,5,5,20,20,10,20,10,5,5,20,10,5,5,5,5,10,5,10,5,5,20,10,5,5,20,5,5,20,5,5,5,5,5,5,5,5,20,10,5,5,5,10,5,5,5,20,5,10,5,5,10,20,5,10,5,20,5,10,5,5,5,5,5,20,5,5,5,5,5,20,5,5,10,10,20,20,5,5,10,20,20,5,20,5,5,5,5,5,5,10,5,20,10,20,20,5,5,5,5,5,5,20,5,10,20,5,5,20,5,5,5,5,20,20,5,5,5,10,10,5,5,5,5,20,5,5,20,5,20,20,5,20,5,5,5,5,20,20,5,10,5,5,10,10,10,5,20,10,10,10,20,10,5,5,5,5,5,10,20,10,20,5,10,5,5,20,10,20,5,20,5,10,5,5,5,20,10,20,5,5,5,10,10,5,10,5,5,5,5,5,20,5,5,20,5,20,20,20,20,5,5,5,10,5,20,5,10,20,20,10,5,20,5,20,5,5,10,5,5,5,5,5,5,5,5,20,5,10,5,5,20,5,20,5,5,5,5,5,20,5,5,10,10,10,5,5,5,10,10,5,5,5,5,5,10,20,5,20,5,20,20,10,5,5,20,10,5,10,5,5,5,5,5,5,20,20,20,20,5,5,5,10,5,10,10,10,5,5,5,5,5,10,5,20,5,20,5,5,5,5,5,5,20,5,5,10,20,10,5,20,20,5,20,20,5,5,5,5,5,10,5,5,10,10,5,5,5,5,5,5,5,5,5,20,5,5,5,10,10,5,5,5,5,5,5,5,10,20,5,5,20,10,5,20,5,5,20,10,10,10,5,10,10,5,5,5,20,10,5,10,20,5,5,10,5,5,5,5,5,5,10,5,5,20,5,5,20,20,10,5,5,5,10,5,5,5,20,5,5,10,5,10,10,20,5,5,20,5,20,20,5,20,5,5,5,5,20,10,5,20,5,20,5,5,20,5,5,10,20,5,20,10,5,5,20,5,20,5,10,5,5,5,10,10,5,20,10,5,20,20,5,20,5,5,20,5,10,5,5,5,5,20,10,5,5,10,5,5,5,20,5,5,5,5,20,5,5,5,10,20,5,5,5,5,5,5,5,5,5,5,10,20,10,5,5,5,5,20,5,5,10,20,5,5,5,5,10,20,5,5,5,10,5,5,5,5,5,20,20,20,5,5,5,5,5,5,20,5,20,20,10,5,10,5,5,5,5,5,5,5,5,10,20,10,20,20,10,5,20,5,10,20,10,20,5,5,10,20,5,5,5,5,20,20,5,10,10,20,5,5,5,5,5,5,20,5,10,5,20,10,5,5,5,5,5,5,5,5,5,5,5,10,5,5,5,5,5,5,5,20,5,20,5,5,5,5,5,5,5,10,10,20,20,5,5,20,10,20,5,10,10,10,20,20,5,20,20,5,10,10,20,5,10,10,5,5,20,5,5,20,10,5,20,20,5,5,20,5,5,5,20,20,5,5,5,5,10,20,5,5,20,5,20,10,10,10,5,20,5,10,10,10,20,20,5,5,5,10,5,20,5,5,5,5,5,5,5,5,5,5,20,5,5,10,5,5,10,5,5,5,5,5,5,5,20,10,20,5,20,5,5,5,5,5,20,5,5,5,20,5,5,5,5,5,20,20,10,5,5,10,5,5,10,10,20,20,5,5,20,10,5,5,5,5,5,20,10,5,5,10,10,5,10,5,10,5,5,20,20,20,10,20,5,5,20,5,5,5,20,20,10,5,5,20,20,5,5,10,5,5,20,5,20,10,10,20,5,5,5,10,20,5,5,20,5,5,5,5,5,10,5,5,20,5,5,20,20,20,5,10,5,5,5,5,5,5,5,5,5,20,5,5,20,5,5,5,10,20,20,10,5,10,5,5,10,10,10,5,5,5,10,5,5,10,5,5,5,20,5,5,10,5,5,5,5,5,5,10,20,10,5,5,20,20,10,5,10,5,5,5,5,5,5,5,5,5,5,5,5,5,20,5,10,20,20,5,10,5,10,10,5,5,5,5,5,20,5,20,10,20,5,20,5,5,5,10,5,10,5,5,5,5,10,5,10,20,5,5,5,10,5,5,10,5,10,5,10,5,10,20,5,5,5,5,5,5,5,5,5,5,10,20,20,20,10,5,5,10,5,5,5,5,20,5,5,20,5,20,5,5,5,5,5,5,5,20,5,10,5,5,20,5,5,20,20,5,20,20,5,10,5,5,5,5,20,5,5,10,20,10,20,5,20,5,20,20,10,5,5,5,5,5,5,10,5,5,20,10,20,5,5,5,5,10,5,20,5,5,5,10,5,20,20,5,20,5,5,20,5,20,5,5,10,5,5,20,5,5,5,5,5,10,20,20,5,5,5,10,5,20,5,10,5,10,20,5,10,5,5,5,5,20,5,10,5,5,5,5,10,10,20,20,20,5,10,5,5,20,5,5,5,5,10,10,10,5,20,5,10,5,10,10,5,20,5,5,10,20,20,5,5,5,5,5,5,5,5,10,20,10,5,5,10,10,20,5,5,5,5,5,20,5,10,5,10,5,5,5,20,10,20,5,10,5,5,5,20,5,5,5,5,5,10,5,5,20,5,5,5,5,5,5,10,5,10,20,5,5,5,10,5,10,5,20,10,20,5,5,5,5,5,5,5,10,20,5,20,20,5,5,10,20,10,5,5,5,5,10,20,5,5,5,5,5,10,10,5,5,5,5,10,5,10,10,10,10,5,5,20,5,5,5,20,5,20,5,10,10,5,5,5,5,5,10,10,20,20,5,5,5,5,10,5,10,5,20,5,5,10,5,5,5,10,10,20,5,10,5,5,5,5,10,20,5,10,5,5,5,10,5,5,5,5,10,5,5,5,20,5,5,10,5,5,5,5,20,20,5,5,5,5,10,5,10,5,10,10,5,5,10,10,5,5,5,10,5,10,20,10,20,20,5,5,5,5,10,5,20,5,5,10,5,5,20,5,5,5,5,20,10,5,10,20,10,20,5,5,5,5,5,5,5,20,20,10,5,5,20,5,20,10,20,10,5,20,5,20,10,20,20,5,5,20,5,20,10,5,5,5,10,5,5,5,5,5,5,5,5,10,10,20,5,5,10,10,20,20,5,10,5,5,5,5,10,5,5,10,5,5,20,5,20,10,5,5,5,20,5,10,5,20,20,5,5,10,10,5,5,5,20,20,5,5,5,20,10,5,5,10,5,5,5,5,5,10,5,10,5,5,5,20,5,10,5,5,5,20,10,5,5,10,5,10,5,5,10,20,10,5,5,20,5,5,20,5,5,5,5,10,5,10,5,5,5,20,5,10,5,10,20,20,20,5,10,20,5,5,5,5,10,5,5,5,10,5,20,20,10,5,5,5,10,5,20,20,5,10,20,10,10,10,20,5,5,20,5,20,10,20,20,5,20,10,10,5,5,10,10,5,10,20,20,5,10,10,5,5,5,5,5,20,5,5,10,10,10,5,10,5,5,10,20,5,20,5,10,5,5,20,20,10,5,10,10,5,20,10,10,5,5,5,20,10,10,20,5,5,20,5,10,5,10,10,20,5,5,5,10,20,10,10,5,5,5,10,5,10,5,20,10,5,5,5,20,5,5,10,20,5,10,10,5,20,5,5,20,5,5,5,20,5,5,5,5,10,10,5,5,10,10,5,20,5,5,10,10,5,5,10,5,20,10,5,20,5,5,5,10,20,5,10,5,20,5,5,5,5,5,10,5,5,10,5,20,5,10,5,5,20,5,5,5,10,5,20,20,20,5,10,5,5,5,5,5,10,20,10,5,5,5,20,10,10,20,5,5,5,5,10,10,5,20,5,20,20,5,20,10,5,20,5,5,5,10,20,20,5,5,5,5,5,5,20,10,20,20,5,5,5,5,5,5,10,10,20,5,5,5,10,5,10,5,10,5,20,10,5,5,5,5,5,20,20,20,5,5,5,5,10,5,5,20,5,10,10,20,5,5,5,10,5,5,20,5,20,5,10,5,5,5,5,5,5,5,5,5,5,5,5,5,10,20,5,20,5,5,5,20,5,20,20,5,5,5,10,5,20,10,5,10,20,5,20,10,5,5,10,20,5,20,5,20,20,5,20,5,10,10,5,5,5,5,20,5,5,20,20,5,5,5,10,20,5,5,20,5,5,5,10,10,5,10,5,20,10,10,5,20,10,20,5,5,5,5,5,5,20,10,20,5,10,5,5,10,20,5,5,10,5,5,20,5,5,5,10,20,10,5,5,20,5,5,5,5,20,20,10,5,20,5,5,5,5,5,5,5,20,5,5,10,20,20,5,5,10,20,5,5,10,5,5,5,5,20,5,5,20,10,5,5,5,20,5,10,5,5,5,10,20,5,10,20,5,5,5,5,5,5,5,10,5,20,5,20,20,5,5,5,5,20,5,20,5,10,5,5,5,5,5,5,5,5,5,5,10,5,10,5,5,20,5,5,20,5,5,20,20,20,5,5,5,5,5,10,5,10,10,20,20,20,5,5,5,20,5,5,5,20,10,5,5,10,5,20,5,10,5,5,10,20,5,20,10,20,20,5,10,10,10,10,10,20,20,20,5,5,5,5,5,20,10,5,5,20,20,5,10,5,10,5,10,10,5,10,5,5,20,5,10,5,10,10,20,5,10,5,20,5,10,5,10,20,10,20,5,5,5,5,5,10,20,5,5,5,5,20,20,5,20,5,5,5,20,5,5,20,5,5,5,5,10,5,5,5,5,5,5,10,5,5,5,5,20,20,10,20,5,5,5,5,5,10,20,10,5,5,5,5,10,5,5,10,5,5,5,5,10,10,20,5,5,20,5,5,10,5,10,5,5,5,5,5,5,20,5,5,20,5,20,5,20,5,20,10,5,5,10,5,20,5,5,5,10,10,20,5,5,5,20,10,20,5,5,5,5,5,10,5,5,5,5,20,10,5,10,20,20,5,20,20,10,20,10,10,10,5,5,10,20,5,10,5,5,20,10,5,10,5,10,10,10,20,20,5,20,5,10,5,10,5,5,5,20,5,20,20,5,10,5,5,5,5,5,20,5,5,5,20,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,10,5,5,20,5,5,10,20,10,10,10,5,10,5,5,10,5,5,5,10,5,5,5,20,20,5,20,5,5,5,20,5,20,5,5,5,20,5,20,20,5,5,10,20,20,5,5,5,20,5,5,20,5,5,20,5,20,10,5,5,5,5,20,10,20,10,20,10,5,5,10,5,5,5,5,5,5,5,5,5,5,10,10,5,20,20,5,20,20,5,10,10,5,5,5,5,5,5,10,20,20,5,5,5,20,5,5,5,5,10,5,5,20,5,5,20,20,20,10,20,5,5,5,10,5,5,20,5,20,20,5,10,20,5,5,10,5,10,5,5,5,5,5,5,5,10,10,5,5,5,5,20,5,5,10,20,5,10,5,10,5,10,20,5,5,5,5,5,10,20,5,10,10,10,5,5,5,5,10,20,20,5,20,20,5,10,5,5,5,10,20,10,5,5,5,5,5,5,5,20,20,5,5,5,5,5,10,5,20,5,20,10,5,10,5,5,5,10,5,10,5,20,5,5,10,5,20,5,5,5,10,5,20,20,20,10,5,10,10,10,5,5,5,5,20,5,20,10,5,5,5,5,5,5,10,5,20,20,10,10,20,5,5,5,10,10,5,20,5,10,20,20,5,20,5,5,5,5,5,10,5,5,5,10,5,10,5,20,5,10,10,10,5,5,10,5,10,5,5,20,5,5,5,5,5,5,10,5,5,10,10,5,20,20,5,5,5,20,5,20,20,5,20,10,10,10,5,5,10,20,10,5,5,20,5,5,10,5,20,5,5,5,5,5,20,5,5,20,10,5,5,5,5,10,5,5,5,20,5,5,20,10,10,5,10,10,5,20,10,20,10,10,10,5,5,10,5,5,5,10,5,5,5,5,5,5,5,5,5,5,20,5,10,5,5,5,5,5,5,5,20,20,20,5,5,5,10,10,5,5,20,20,5,5,5,20,10,20,5,5,20,5,5,20,10,20,5,5,20,10,10,20,20,5,5,20,20,5,5,20,5,5,5,5,5,10,5,5,20,5,5,20,20,5,20,5,10,5,5,20,5,20,10,5,5,5,5,5,5,10,5,5,5,20,5,5,10,20,10,5,5,20,10,10,20,20,5,10,10,20,20,5,5,20,20,5,10,5,5,5,5,5,5,5,5,5,10,20,5,5,5,5,20,10,10,20,20,5,5,20,10,5,5,10,5,5,20,10,5,20,5,10,10,5,5,10,20,5,20,5,5,20,5,5,10,5,5,10,5,5,10,5,5,5,5,5,10,5,5,20,20,20,5,5,5,5,5,5,10,5,20,10,5,10,20,5,5,5,10,10,20,5,10,10,10,10,5,5,20,5,5,5,10,5,5,10,10,20,5,5,10,10,20,10,5,5,5,5,20,20,5,20,5,20,5,10,5,5,5,5,5,5,5,20,5,5,5,5,10,5,20,10,5,5,20,5,20,10,5,5,5,5,20,5,20,10,5,5,5,10,20,5,10,10,5,5,5,5,10,5,20,5,5,5,20,10,5,10,5,10,5,5,10,5,5,5,5,5,10,5,20,5,10,5,20,20,5,5,5,5,10,5,10,5,5,20,5,10,5,10,5,5,20,5,10,5,20,20,5,20,5,20,5,5,5,5,20,10,5,5,5,5,10,5,10,10,20,20,5,5,5,10,5,20,5,10,10,5,5,20,5,5,5,5,10,10,10,10,10,20,5,10,5,20,5,10,20,10,10,5,5,5,5,5,10,5,5,5,5,10,5,10,10,20,5,5,5,5,20,5,20,20,20,5,5,5,5,5,10,5,5,5,20,5,5,5,5,20,20,5,10,10,5,5,20,20,5,10,5,10,10,5,10,20,20,5,10,20,10,20,5,5,5,10,20,5,10,5,5,5,20,5,10,5,5,5,5,20,10,10,5,5,5,10,5,20,5,5,5,5,5,10,5,5,5,5,5,5,10,10,5,10,5,10,5,5,5,5,5,20,10,5,5,20,10,20,5,10,20,10,5,5,5,5,20,10,20,5,10,10,5,10,20,5,20,5,20,5,5,5,5,5,5,10,5,5,5,5,5,5,5,10,20,10,20,5,20,5,5,10,20,5,5,5,5,20,20,20,10,5,5,5,5,20,5,5,5,5,5,10,5,20,5,5,10,20,5,20,5,5,5,5,20,10,10,5,10,10,5,5,5,10,20,20,20,5,5,5,10,5,5,20,5,10,10,5,10,5,5,10,5,10,5,5,5,20,10,10,20,5,20,5,5,5,10,5,10,5,5,20,5,10,5,20,5,20,5,10,5,5,5,5,10,5,5,5,5,5,5,5,5,5,5,20,20,5,10,5,5,20,5,20,10,10,20,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,20,5,5,5,20,5,5,5,20,5,5,20,20,5,5,5,20,10,5,5,20,5,5,5,5,5,5,20,10,5,5,5,5,10,5,5,5,20,5,5,20,5,10,5,5,10,20,10,5,20,5,5,5,10,20,10,5,10,5,5,5,5,5,20,20,20,20,5,20,20,5,5,5,10,10,5,20,5,20,5,5,5,20,10,5,5,5,20,10,5,20,5,20,20,5,5,10,5,5,5,5,5,5,10,20,10,20,5,5,10,5,20,5,5,10,10,5,5,5,20,10,10,5,5,10,5,5,5,20,5,20,5,5,20,5,20,10,20,20,5,5,10,5,5,20,5,10,5,5,5,10,5,5,5,5,5,5,5,10,5,5,5,5,20,5,5,5,5,5,5,20,10,5,10,5,5,5,20,20,10,5,5,5,5,20,5,5,10,10,5,5,10,10,5,10,5,5,10,10,5,5,5,20,10,10,5,10,5,5,20,5,5,20,5,5,10,20,5,10,5,5,5,5,5,5,5,5,20,5,20,5,10,5,5,10,5,5,5,10,5,5,10,10,10,5,5,20,20,5,5,5,5,20,5,5,5,5,10,20,5,10,10,5,5,20,20,5,5,5,5,5,20,20,10,20,20,10,10,5,20,20,5,5,20,10,10,20,5,5,5,5,5,5,20,5,5,10,20,5,5,5,5,5,20,10,10,5,5,5,5,5,10,5,20,5,5,5,20,10,10,10,5,10,5,5,5,20,5,10,20,20,5,5,5,5,20,10,10,10,20,5,5,20,5,5,5,5,5,10,5,20,5,10,5,20,5,5,20,10,20,5,5,10,5,5,5,5,5,5,5,5,20,20,5,5,20,5,10,10,5,5,10,10,20,5,5,20,10,10,20,5,20,5,5,10,5,10,5,20,10,5,5,10,10,5,5,5,5,20,5,10,5,10,5,10,20,5,5,10,20,5,10,5,5,5,10,5,5,10,5,10,10,5,20,10,5,5,5,20,5,10,5,5,5,5,5,20,5,20,20,5,20,5,5,10,5,20,5,5,20,20,20,20,10,5,10,5,5,20,10,5,5,10,5,5,5,5,5,10,5,5,5,5,5,5,5,5,5,10,5,5,5,5,10,10,5,5,5,5,5,5,5,10,5,5,5,5,5,10,5,5,20,10,20,10,10,20,20,5,5,10,5,5,5,10,5,10,5,5,10,5,5,5,5,10,10,5,10,5,20,5,20,5,5,5,5,5,20,5,10,20,5,20,10,5,5,5,5,10,10,20,10,20,5,10,5,20,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,10,20,5,20,5,5,5,5,10,5,5,5,5,5,10,10,10,20,10,10,20,5,5,20,5,10,5,5,5,5,5,5,5,20,10,5,20,5,10,20,10,20,5,5,5,5,5,5,20,5,5,20,20,5,10,5,5,10,5,5,20,5,5,5,20,5,20,10,5,5,5,10,10,20,5,10,10,5,20,10,5,5,10,20,20,5,5,5,5,10,5,5,10,20,5,10,5,10,5,5,10,5,20,5,10,5,20,20,10,5,20,10,5,5,5,10,10,10,20,20,5,20,10,5,5,5,5,5,20,5,10,5,5,10,10,5,10,5,5,10,20,5,5,5,5,5,5,10,5,20,10,20,20,5,5,5,10,5,20,5,5,5,5,5,5,5,5,20,10,5,5,20,5,5,20,5,20,5,5,5,10,5,5,5,5,5,5,5,5,10,5,5,10,5,20,10,5,20,5,5,10,5,5,20,5,5,10,5,20,5,5,10,5,20,5,10,5,20,20,5,5,5,20,20,5,5,5,20,5,5,20,10,20,5,5,5,10,5,5,5,5,10,5,5,5,20,20,5,5,5,20,5,10,10,10,5,5,5,5,20,5,5,10,5,20,5,5,5,5,5,5,5,10,5,5,5,20,5,5,10,5,5,5,5,5,5,20,5,5,5,5,5,10,20,5,5,20,5,20,5,5,20,10,5,5,5,20,10,5,20,20,5,5,5,5,20,20,5,5,5,5,5,20,5,10,10,5,20,5,10,5,5,10,5,20,20,5,5,20,5,10,5,5,20,5,10,10,5,5,5,5,5,5,5,5,20,20,5,20,20,5,5,5,5,5,5,10,5,5,5,5,5,5,10,5,5,20,5,5,5,20,5,5,20,20,5,5,5,10,5,10,20,5,5,5,5,10,5,5,10,5,5,10,5,5,20,5,5,5,5,5,5,5,10,5,5,20,5,5,10,5,5,5,5,5,5,5,5,20,10,5,5,5,5,5,5,20,10,5,10,5,10,5,10,20,20,20,10,5,5,10,5,10,5,5,5,5,5,5,5,5,10,5,10,5,5,5,5,10,10,20,20,5,5,20,5,5,10,20,20,10,5,5,5,5,5,5,20,5,5,10,20,20,10,5,5,5,5,5,5,5,20,10,5,5,10,5,5,5,10,5,5,20,20,5,5,5,5,20,5,20,5,5,5,5,5,5,10,5,5,5,5,5,5,5,5,5,5,20,5,10,20,20,20,10,5,5,5,5,10,5,5,20,20,5,20,5,10,5,5,5,5,5,5,20,10,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,20,5,5,20,10,10,5,5,5,5,5,5,20,10,5,20,5,20,5,5,5,5,5,10,5,5,20,20,5,10,20,5,10,5,20,5,5,5,5,5,5,10,20,5,5,5,10,10,5,20,5,5,10,5,5,10,10,5,5,20,10,5,5,20,10,10,5,5,20,5,5,5,20,5,10,10,5,5,5,5,5,5,5,20,10,20,20,5,20,5,5,5,5,5,5,5,20,10,10,5,5,5,5,20,5,5,20,5,10,5,5,5,10,20,10,5,20,20,10,20,10,20,10,5,5,5,5,5,10,10,5,5,5,5,10,10,5,5,5,5,5,5,5,5,5,10,5,10,5,5,20,20,10,5,5,20,5,5,5,5,5,5,5,5,20,20,5,10,20,10,5,10,5,20,5,5,10,5,10,20,5,5,5,20,5,5,5,5,10,5,20,20,5,5,20,20,10,20,20,10,5,5,5,5,10,10,5,20,10,5,5,20,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5,5,5,20,5,5,10,20,5,10,5,5,10,20,5,5,10,5,5,20,5,5,10,10,5,5,5,5,5,5,5,5,5,5,20,5,5,10,10,20,5,5,10,5,5,5,20,5,20,5,20,5,5,10,5,20,5,5,5,5,5,5,5,10,5,10,5,20,5,20,5,10,5,5,5,5,10,5,5,5,10,5,20,5,5,5,5,5,20,5,5,5,5,10,5,5,10,10,10,20,5,5,20,20,5,5,5,5,5,5,5,5,5,20,10,5,10,20,5,5,5,5,5,5,20,5,20,5,10,10,5,5,5,20,5,5,5,5,5,5,10,10,5,5,5,5,5,5,20,5,5,5,5,20,5,5,20,5,10,20,5,10,10,5,5,5,5,20,10,5,5,5,5,20,20,20,5,5,5,10,5,5,5,5,10,5,5,5,20,20,5,20,5,5,10,5,5,5,5,20,10,5,10,5,5,5,5,5,5,5,20,5,10,5,10,5,5,5,5,20,20,5,5,5,20,5,5,5,20,5,10,5,5,10,5,5,5,5,5,10,20,5,10,10,5,5,10,5,5,5,10,20,5,20,5,10,5,5,10,5,5,5,5,5,5,5,5,5,5,20,5,5,5,5,5,5,5,5,10,20,10,20,5,10,20,5,5,10,5,5,5,5,10,5,10,20,5,5,20,10,5,20,20,5,5,5,5,5,5,5,5,5,10,5,5,5,20,5,20,20,5,5,5,5,10,5,20,5,20,5,5,5,20,5,20,5,5,20,10,5,10,5,5,10,5,5,5,5,5,5,5,10,10,10,20,10,5,5,10,5,20,5,20,5,20,5,5,5,5,10,5,5,10,5,5,5,5,5,5,20,5,20,5,5,5,20,5,20,20,20,5,5,5,20,5,10,20,5,10,20,20,5,5,5,20,5,5,5,5,10,5,20,20,5,5,5,20,10,5,5,20,5,20,5,5,20,20,5,10,5,5,20,10,20,10,10,20,5,5,10,10,20,10,5,5,5,10,20,5,5,20,5,20,5,10,5,5,20,20,5,5,5,5,5,5,5,10,20,5,5,5,20,5,5,20,5,20,5,20,5,5,10,5,5,10,10,5,5,5,5,5,20,10,10,5,5,5,20,10,5,5,5,5,20,20,5,10,10,5,5,5,10,5,5,10,20,20,5,5,10,10,10,5,5,5,5,5,20,10,5,5,5,20,20,20,20,20,5,5,5,20,10,20,20,5,5,5,10,20,5,10,10,5,10,5,5,10,5,10,20,5,5,10,5,20,5,5,20,5,5,5,20,5,5,5,5,10,20,10,10,5,5,10,5,5,5,10,5,5,20,20,20,20,5,5,20,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,20,20,10,20,5,20,10,10,5,5,10,5,5,20,5,20,5,10,5,10,5,5,10,10,20,20,20,5,10,5,10,5,20,10,5,5,5,20,20,20,20,5,5,5,5,10,5,5,5,5,20,5,5,10,10,20,5,5,10,5,10,5,5,20,10,20,5,5,5,10,5,5,20,5,5,20,10,5,5,10,10,5,10,5,5,5,20,10,5,10,20,5,5,5,5,5,20,5,5,5,20,5,5,5,20,10,5,20,10,10,20,5,5,5,5,5,5,5,5,5,10,5,5,5,5,5,5,20,5,5,5,5,5,5,20,5,5,5,20,5,20,5,20,20,10,5,10,20,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,20,5,5,5,20,5,5,20,5,5,5,5,20,5,20,10,5,5,5,5,5,5,5,5,5,20,5,5,20,20,5,5,5,5,5,5,5,5,5,5,20,5,5,5,20,5,20,10,5,20,5,5,5,20,20,5,10,5,10,5,10,10,10,5,5,5,5,5,5,5,5,10,10,5,10,5,20,10,5,5,5,5,5,5,10,5,5,20,5,10,5,5,20,5,10,5,5,20,5,20,5,5,20,20,20,5,5,20,5,20,5,20,5,5,20,5,5,5,5,10,5,5,5,10,5,10,10,5,5,5,5,5,5,5,20,10,5,5,5,20,5,20,5,5,20,5,5,5,5,5,5,20,5,5,20,20,5,5,5,10,5,5,5,10,5,20,5,5,20,5,5,5,5,10,5,10,5,10,10,5,5,10,5,20,20,10,5,10,10,20,5,10,5,5,5,10,5,10,5,5,5,10,5,20,5,5,5,10,20,20,5,5,10,5,20,5,20,5,10,5,10,5,5,5,5,10,5,5,5,5,5,5,20,5,5,5,5,5,20,5,5,10,5,5,5,5,5,10,5,20,5,5,20,5,20,5,5,20,5,20,5,5,10,5,5,5,5,5,5,20,20,5,10,5,10,5,5,5,10,5,5,5,20,5,5,5,10,5,5,5,10,10,5,20,5,5,10,5,5,5,20,5,5,10,5,10,5,10,5,5,5,5,5,20,10,10,5,20,5,5,5,10,10,5,5,5,10,10,5,5,20,5,5,5,5,5,5,5,10,5,20,10,20,5,5,5,5,5,5,20,10,5,20,20,10,5,5,10,10,10,5,10,5,10,20,20,20,20,10,5,5,20,20,20,5,20,20,5,5,5,5,5,10,5,5,5,5,10,20,5,10,10,5,5,5,5,10,5,5,5,5,20,10,5,5,5,20,20,5,10,5,10,5,20,5,5,5,10,5,5,10,20,5,5,20,5,5,10,5,20,5,10,5,10,10,10,10,5,5,20,5,20,20,5,20,20,5,10,20,5,5,5,5,5,5,5,20,20,5,10,10,10,5,5,5,10,5,5,5,20,5,5,5,10,20,5,10,20,10,20,10,5,5,5,5,10,10,5,5,20,20,20,5,20,20,5,5,20,5,10,5,10,5,5,5,5,5,5,5,20,5,10,10,5,20,10,5,5,5,5,5,5,10,5,5,5,20,5,5,5,5,5,20,20,5,5,5,5,10,20,10,5,5,20,20,10,20,20,20,5,10,20,5,5,10,10,20,10,10,5,5,20,5,5,5,20,5,5,5,5,20,10,5,10,5,10,10,10,10,5,5,5,20,5,5,5,5,5,5,5,20,5,20,5,10,10,10,5,5,5,10,5,5,20,20,5,5,20,5,10,10,20,20,5,5,10,10,5,5,20,5,5,5,5,10,20,5,5,5,10,20,5,5,20,5,5,5,5,10,10,5,5,20,5,5,5,20,5,5,5,5,5,5,5,20,20,5,5,5,5,20,20,20,10,5,5,5,5,10,20,5,20,20,20,5,5,5,5,10,20,5,5,5,5,5,5,5,20,5,5,5,10,20,20,5,5,5,5,20,5,20,5,5,5,5,5,5,10,10,10,5,20,10,5,5,20,20,5,20,10,5,10,5,20,20,5,10,5,5,5,5,5,5,5,5,5,20,20,5,20,20,5,20,10,10,20,5,5,20,5,5,5,5,10,5,5,5,10,5,5,10,10,20,10,5,5,5,5,5,10,5,5,5,5,10,5,10,5,5,5,5,5,5,5,5,10,10,5,5,10,5,10,10,5,5,20,20,10,10,5,5,20,20,5,5,5,5,5,10,20,10]
print (lemonadeChange(bills))