# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 14:19:44 2021

@author: VIP
"""

class FirstUnique:
    from queue import Queue
    from collections import defaultdict
    def __init__(self, nums: List[int]):
        self.queue= Queue(int)
        self.d = defaultdict(int)
        self.queue.put(nums)
        for i in nums:
            d[i] +=1
            
        #print (self.queue)
        
    def showFirstUnique(self) -> int:
        found = False
        while (Qsize(self.queue >1):
            if self.d[i] ==1:
                return i
        return -1
        
    def add(self, value: int) -> None:
        self.queue.append(value)
        if value in self.d.keys():
            self.d[value] +=1
        else:
            self.d[value] =1
        #print (self.queue)
        