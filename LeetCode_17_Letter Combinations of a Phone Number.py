# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 14:11:27 2021

@author: VIP
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        ln = len(digits)
        
        if ln ==0:
            return None
        
        import itertools
        result =[]
        d = {
            '1':[None],
            '2':['a','b', 'c'], 
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p', 'q','r','s'], 
            '8':['t','u','v'], 
            '9':['w','x','y','z']
            
            }
        raw_input = []
        for i in digits:
            raw_input.append(d[i])
        tempResut =  list (itertools.product(*raw_input))
        for i in tempResut:
            result.append( "".join(i))
        return result 
    
        