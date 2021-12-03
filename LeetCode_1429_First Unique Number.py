# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 07:24:12 2021

@author: VIP
"""

class FirstUnique:
    from collections import defaultdict
    def __init__(self, nums: List[int]):
        self.queue= []
        self.d = defaultdict(int)
        self.queue.extend(nums)
        for i in nums:
            self.d[i] +=1

    def showFirstUnique(self) -> int:
        #print (self.d)
        if 1 not in self.d.values():
            return -1
        for i in self.queue:
            if self.d[i] ==1:
                return i
        return -1
        
    def add(self, value: int) -> None:
        self.queue.append(value)
        self.d[value] +=1
        