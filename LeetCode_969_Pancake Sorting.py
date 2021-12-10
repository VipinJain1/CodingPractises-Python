# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 14:36:08 2021

@author: VIP
"""

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ln = len(arr)
        if ln <=0:
            return 0
        if arr == sorted(arr):
            return []
        
        end  = ln
        start = 0
        result = []
        while(start <end):
            mx= max(arr[start:end])
            mxindex = arr.index(mx)
            result.append(mxindex+1)
            arr[0:mxindex+1] = arr[0:mxindex+1][::-1]
            arr[start:end] = arr[start:end][::-1]
            result.append(end)
            end -=1
        print (arr)
        return result
        
        