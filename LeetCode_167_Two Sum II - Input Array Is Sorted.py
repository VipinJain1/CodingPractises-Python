# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 10:49:40 2021

@author: VIP
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        cnt =0
        end = len(numbers) -1
        found = False
        while (cnt <end):
            if numbers[cnt]+ numbers[end] == target:
                found = True
                return [cnt+1,end+1]
            if numbers[cnt]+ numbers[end]> target:
                end -=1
            elif numbers[cnt]+ numbers[end] < target:
                cnt +=1
        if not found:
            return None