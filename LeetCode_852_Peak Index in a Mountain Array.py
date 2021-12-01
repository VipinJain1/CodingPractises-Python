# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 13:59:07 2021

@author: VIP
"""

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        ln = len(arr)
        if ln <3:
            return None
        start =1
        end = ln
        while (start <end):
            if arr[start] < arr[start-1]:
                return start -1
            start +=1
            
        
        