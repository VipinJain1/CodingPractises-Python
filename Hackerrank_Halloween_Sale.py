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
    
    origBasePrice = m
    origtotalMoney = s
    originitailCost =p 
    
    if initailCost > totalMoney:
        return 0
    
    if  initailCost <=0 or totalMoney <=0:
        return  0
    if basePrice <=0:
        basePrice=1
    
    if origBasePrice == originitailCost:
        return origtotalMoney//origBasePrice
        
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
        try:
            if initailCost - discountToApply ==0: 
                totalGames = totalGames + totalMoney//1
            else:
                totalGames = totalGames + totalMoney//(initailCost - discountToApply)
        except:
            return totalMoney
    if totalGames <0:
        return 0
    else:
        return totalGames

p =11 # initail cost of game
d =11  # to give further discount after each purchase
m =1  # base price to sell
s =9981 # total money

print (howManyGames(p, d, m, s))