# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 08:33:50 2021

@author: VIP
"""


def threeSum(nums):
     ln = len(nums)
     if ln <3:
         return
     d  =dict()
     res = set()
     for i in range (0,ln):
         for j in range (i+1, ln):
             sm = nums[i] + nums[j]
             if sm in d.keys():
                 d[sm] += [(i,j)]
             else:
                 d[sm] = [(i,j)]
     #print (d)
     for i in range (0,ln):
         val = -nums[i]
         if  val in d.keys():
             for data in d[val]:
                 if i not in data:
                     row = tuple(sorted([nums[i], nums[data[0]],nums [data[1]]]))
                     res.add(row)
     return res
             
       
nums = [-1,0,1,2,-1,-4]     
res= threeSum(nums)      
print (res)