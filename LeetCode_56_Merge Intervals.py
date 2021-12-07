# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 08:29:21 2021

@author: VIP
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ln  = len(intervals)
        if ln ==0:
            return 0
        # o(nlogn)
        intervals.sort(key = lambda x:x[0])
        #print (intervals[-1][1])
        res  = []
        res.append(intervals[0])
        #o(n)
        for start,end in intervals[1:]:
            lastEnd  = res[-1][1]
            if start <= lastEnd:
                end = max(lastEnd, end)
                res[-1][1] = max([start,end])
            else:
                res.append([start,end])
        return res
        