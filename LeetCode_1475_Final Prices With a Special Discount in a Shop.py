# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 19:10:22 2021

@author: VIP
"""

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ln = len(prices)
        if ln ==0:
            return None
        if ln ==1:
            return prices
        result =[]
        discount = False
        for i in range (0,ln):
            discount = False
            for j in range (i+1, ln):
                if prices [j] <= prices [i]:
                    discount = True
                    result.append(prices[i] - prices [j])
                    break
            if discount ==False:
                result.append(prices[i])
                
        return result
    
                    
            
        