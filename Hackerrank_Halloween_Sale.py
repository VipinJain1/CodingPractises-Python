# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 14:03:15 2021

@author: VIP
"""

p =20 # initail code of game
d =3  # to give further discount after each purchase
m =0  # base price to sell
s =80 # total money


p = 100 
d = 19 
m = 1 
s = 180

def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    
    initailCost = p
    discountToApply = d
    basePrice = m
    totalGames =  1
    totalMoney = s
    IsDiscountApplied = False 
    
    if initailCost > totalMoney:
        return 0
    
    if  p ==0 or m==0 or s ==0:
        return  0
    
    
    if basePrice == initailCost:
        return totalMoney//basePrice
        
    totalMoney = totalMoney - initailCost
   
    while (totalMoney >= basePrice):
        
        if ((totalMoney >= (initailCost - discountToApply)
            and (initailCost - discountToApply) >= basePrice)):
            
            initailCost = initailCost - discountToApply
            totalMoney = totalMoney - initailCost
            totalGames = totalGames + 1
            IsDiscountApplied = True
        else:
            break 
            
    if IsDiscountApplied == True:
        
        if (totalMoney):
            totalGames = totalGames + totalMoney//basePrice
    else:
        totalGames = totalGames + totalMoney//(initailCost - discountToApply)
            
    return totalGames

print (howManyGames(p, d, m, s))