# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 12:40:04 2021

@author: VIP
"""

import heapq
heap = []
heapq.heappush(heap, 4)
heapq.heappush(heap,2)
heapq.heappush(heap, 6)
heapq.heappush(heap, 5)
heapq.heappush(heap, 6)
heapq.heappush(heap, 1)
print (heap)
type (heap)

            

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()