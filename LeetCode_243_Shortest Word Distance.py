# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 10:54:36 2021

@author: VIP
"""

class Solution:
class Solution:
    def shortestDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:
        idx1 =int()
        idx2 =int()
        lw =  len(wordsDict)
        lw1  = len(word1)
        lw2  = len(word2)
        mn = lw
        i =0   

        while (i<lw):
            try:
                if word1 in wordsDict[i:]:
                    idx1 = wordsDict[i:].index(word1) +i
                if word2 in wordsDict:
                    idx2 = wordsDict[i:].index(word2) +i
                if mn > abs(idx1 - idx2):
                        mn = abs(idx1 - idx2)
                i = i+1
            except:
                return mn
            
        return mn 
    
    

    
        
        
        
wordsDict = ["practice", "makes", "perfect", "coding", "makes", "practice", "makes", "hello", "coding", "makes"]
word1 = "practice"
word2 = "hello"

obj = Solution()
res = obj.shortestDistance( wordsDict, word1, word2)
print (res)