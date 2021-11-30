# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 12:12:17 2021

@author: VIP
"""

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        ln = len(intervals)
        #start=0
        
        start = [i[0] for i in intervals]
        end =   [i[1] for i in intervals]
        start.sort()
        end.sort()
        print (start)
        print (end)
        
        s =0
        res  = 0
        cnt = 0
        e =0
        while (s <ln):
            if start[s] < end[e]:
                cnt +=1
                s +=1
            else:
                cnt -=1
                e +=1
               
            res  = max(cnt,res)
        return res
    