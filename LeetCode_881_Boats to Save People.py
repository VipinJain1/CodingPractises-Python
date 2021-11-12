# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 20:18:50 2021

@author: VIP
"""

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ln = len(people)
        i =0
        boats =0
        people.sort()
        while (i <ln):
            if people[i] + people[ln-1] <=limit:
                i +=1
                ln -=1
            else:
                ln -=1
                
            
            boats +=1
        
        return boats 
                
            
        