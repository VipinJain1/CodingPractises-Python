# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 14:03:15 2021

@author: VIP
"""


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
    
    if  initailCost <=0 or totalMoney <=0:
        return  0
    if basePrice <=0:
        basePrice=1
    
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
            
    if totalGames <0:
        return 0
    else:
        return totalGames

p =10000 # initail cost of game
d =10009  # to give further discount after each purchase
m =1000  # base price to sell
s =180000 # total money

print (howManyGames(p, d, m, s))