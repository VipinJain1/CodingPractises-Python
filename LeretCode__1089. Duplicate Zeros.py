# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 18:27:10 2021

@author: VIP
"""

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        
        """
        ln = len(arr)
        print (ln)
        cnt  =0
        while (cnt <ln):
                if arr[cnt] ==0:
                    arr.insert(cnt+1,0)
                    cnt +=2
                else:
                    cnt +=1
        del  arr[ln:]
            
        
