# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 08:47:33 2021

@author: VIP
"""

# First Solution Time exceed Error:
    
class FreqStack:
    import heapq
  
    def __init__(self):
        self.stack = []
     
    def push(self, val: int) -> None:
        self.stack.insert(0,val)
    def pop(self) -> int:
        from collections import Counter
        #print (self.stack)
        cntr = Counter(self.stack)
        top=cntr.most_common(1)
        val = top[0][0]
        #print ("val to pop",val)
        self.stack.remove (val)
        return val
        

# Second Solution - No Issue

class FreqStack:
    def __init__(self):
        self.heap  = []
        self.numCount = collections.defaultdict(int)
        self.counter =0

    def push(self, val: int) -> None:
        self.numCount[val] +=1
        self.counter +=1
        heapq.heappush(self.heap, (-self.numCount[val], -self.counter, val))
       
    def pop(self) -> int:
        _,_,num = heapq.heappop(self.heap)
        self.numCount[num] -=1
        return num

            