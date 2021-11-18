# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 16:44:18 2021

@author: VIP
"""


class Solution:
    def sumEvenAfterQueries(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        ln = len(nums)
        if ln <=0:
            return None
        
        totalSum = int()
        result  = []
        #First get initial level sum
        for i in nums:
            if i%2 ==0:
                totalSum = totalSum +i
        
        for  i in queries:
            index = i[1]
            new = i[0]
            # Orig vale in list
            orig = nums[index]
            # val to update in list as below
            val = new + orig
            # check all condisiton and see  how the total sum will be affected by new  value.
            if val %2 ==0 and orig %2 ==0:
                totalSum = totalSum + val -orig
                
            elif val %2 ==0 and orig%2 !=0:
                totalSum = totalSum + val
            elif val %2 !=0 and orig%2 ==0:
                totalSum = totalSum - orig
            
            # update the new value into list
            nums[index]= val
            result.append(totalSum)
            
        return result    
            
            
                
            
        
            
nums = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]
            
obj = Solution()
ret = obj.sumEvenAfterQueries(nums,queries)
print (ret)