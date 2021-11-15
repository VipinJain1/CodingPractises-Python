# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 13:21:19 2021

@author: VIP
"""

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        lower =0
        ln = len(piles)
        upper  = ln -2
        print (piles)
        my_coins = int ()
        while (lower <upper):
            my_coins  = my_coins + piles[upper]
            upper = upper-2
            lower = lower +1
        
        return my_coins
            
            
            
        
            