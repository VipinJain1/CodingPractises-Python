# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 11:10:42 2021

@author: VIP
"""

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        ln = len(intervals)
        if ln <=1:
            return True
      
        intervals.sort()
        
        for i in range(1,ln):
            if intervals[i-1][1] > intervals[i][0]:
                return False
        return True
        
        