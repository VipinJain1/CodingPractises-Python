# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 08:33:50 2021

@author: VIP
"""

import time


nums  =[0,-1,0,0,0,2,1,2,3,4,0,-2,2,0,1]
#nums = [1,0,-1,0,-2,2]
#nums  =[2,2,2,2,2]
nums  =[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]

nums  =[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2]
target = 8

print (time.ctime())

nums = sorted(nums)
res = set()
d = dict()
ln  =len(nums)

for i in range (0,ln):
    for j in range (i+1, ln):
        val =  nums[i]+nums[j]
        if val < target and i !=j:
            if val not in d.keys():
                d[val] = [(i,j)] 
            else:
                d[val] += [(i,j)]
for i in range (0,ln):
    for j in range (i+1, ln):
      val =  nums[i] + nums[j]
      expectedVal = target - val
      if (expectedVal) in d.keys():
          expectedPairs = d[expectedVal]
          pair = (i,j)
          for key in expectedPairs:
              if pair != key:
                  data = tuple(sorted((nums[i], nums[j], nums[key[0]], nums[key[1]])))
                  res.add(data)
print (list(res))
print (time.ctime())
    
        
         
         
          
         
          
         