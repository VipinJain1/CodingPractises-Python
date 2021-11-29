# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 12:12:18 2021

@author: VIP
"""

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        ln = len(arr)
        if ln <3:
            return False
        
        start =0
        end =ln-1
        increase = True
        decrease = False
        if arr[0] >= arr[1]:
            return False
        while (start <end):
            if increase:
                while (arr[start] < arr[start+1]):
                    if start +1 ==end:
                        break
                    start +=1
                if arr[start] >= arr[start+1]:
                    increase = False
                    decrease = True

            if decrease:
                while (arr[start] > arr[start+1]):
                    if start+1 ==end:
                        break 
                    start +=1
                    
                if arr[start] <= arr[start+1]:
                    return False
            start +=1

        if decrease == False:
            return False
        return True         
             