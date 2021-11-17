# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 16:59:16 2021

@author: VIP
"""

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        
        ln = len(startTime)
        cnt =0
        total =0
        while (cnt <ln):
            if queryTime <= endTime[cnt] and queryTime >= startTime[cnt]:
                total +=1
            cnt +=1
            
        return total
            
            
        