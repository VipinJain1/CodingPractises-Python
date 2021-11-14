# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 10:49:08 2021

@author: VIP
"""

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        result =[]
        sortedScore = score[:]
        sortedScore.sort(reverse = True)
        
        d ={0:"Gold Medal", 1:"Silver Medal", 2:"Bronze Medal" }
     
        for val in score:
            index = sortedScore.index(val)
            if index in d.keys():
                result.append(d[index])
            else:
                result.append(str(index+1))
                
        return result
        
            
        
        
        