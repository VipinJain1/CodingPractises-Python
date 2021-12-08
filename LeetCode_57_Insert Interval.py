# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 13:38:57 2021

@author: VIP
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ln = len(intervals)
        
        intervals.append(newInterval)
        intervals.sort()
        
        res  = []
        res.append(intervals[0])
        
        for start, end in intervals[1:]:
            lastEnd =   res[-1][1] 
            if start <= lastEnd:
                res[-1][1] = max (lastEnd,end)
                print (res)
            else:
                res.append([start,end])
        
        return res
    
                