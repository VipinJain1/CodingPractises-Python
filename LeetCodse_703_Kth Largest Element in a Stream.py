# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 08:30:13 2021

@author: VIP
"""
class KthLargest:
    import heapq
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums= []
        for i in nums:
            self.add(i)
       
    def add(self, val: int) -> int:
        heapq.heappush(self.nums,val)
        while (len(self.nums) >self.k):
            n = heapq.heappop(self.nums)
        return self.nums[0]
           
  
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

