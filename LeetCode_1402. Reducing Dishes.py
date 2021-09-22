# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 15:13:00 2021

@author: VIP
"""

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        ln = len(satisfaction)
        sts =  sorted (satisfaction)
        if ln ==0:
              return 0
        if len (list (filter (lambda x: x>0, sts))) == 0:
              return 0
        total = 0
        cnt =1
        if all (i >0 for i in sts):
            for i in sts:
                total = total + i*cnt
                cnt +=1
            return total

        else:
            mx =0
            total =0
            for i in range (0,ln):
                cnt =1
                total = 0
                for j in  range (i, ln):
                    total = total + sts[j]*cnt
                    cnt +=1

                if mx < total:
                    mx = total
            return mx    




                
        
                                        
satisfaction = [-1,-8,0,5,-9]

print (maxSatisfaction(satisfaction))