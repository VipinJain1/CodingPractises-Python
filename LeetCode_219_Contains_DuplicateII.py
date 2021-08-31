# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 23:00:46 2021

@author: VIP
"""

"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        ln = len(nums)
        
        if ln <=1 or k ==0:
            return None
        
        found = False
        for i in range (0,ln):
            for j in range (i+1, ln):
                if (nums[i] == nums[j] and abs (i-j) <=k):
                    found = True
        return found
    
"""


                  

        
def containsNearbyDuplicate(nums,k):
    d = dict()
    found = False
    for count, i in enumerate (nums):
        if i in d.keys():
            d[i].append(count)
        else:
            d[i] = [count]
    for i in d.values():
        dist = i[0]
        if len(i) >1:
            for j in range (1,len(i)):
                if 
            
                
            
                found = True
                return found
    return found
        

    
nums =[1,2,3,1]
k =3
print (containsNearbyDuplicate(nums,k)) 
   