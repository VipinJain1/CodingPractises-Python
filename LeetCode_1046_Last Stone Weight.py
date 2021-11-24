# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 18:09:59 2021

@author: VIP
"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #stones.sort()
        end =len(stones)
        if end ==0:
            return 0
        import heapq
        heapq._heapify_max(stones)
        while (len(stones)):
            if len(stones) ==1:
                return stones[0]
            a = heapq._heappop_max(stones)
            b = heapq._heappop_max(stones)
            if a!=b:
                stones.append(abs(a-b))
        return 0
    