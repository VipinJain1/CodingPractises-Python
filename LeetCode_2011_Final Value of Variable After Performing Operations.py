# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 09:11:29 2021

@author: VIP
"""

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        l  = len(operations)
        if  l ==0:
            return
        
        x =0
        for i in operations:
            if i[0:2] == '--':
                x -=1
            elif i[0:2] == '++':
                 x +=1
            elif i[1:3] == '++':
                x +=1
            elif i[1:3] == '--':
                 x -=1
            else: 
                return False
            
        return x
    
            