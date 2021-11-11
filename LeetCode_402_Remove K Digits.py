# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 11:27:20 2021

@author: VIP
"""

class Solution:
    def removeKdigits(self, num1: str, k: int) -> str:
        cnt =0
        
        num = list(num1)
        i = 0
        while cnt<len(num):
            if num[i] > num[i+1]:
                del num[i]
            else:
                del num[i+1]
            cnt +=1
            if cnt ==k:
                return  str(int ("".join(num)))
            
            
                
num = "43268346263284747248244840494242423924326834626328474724824484049424242392"
k =8
obj = Solution()
res = obj.removeKdigits(num,k)
