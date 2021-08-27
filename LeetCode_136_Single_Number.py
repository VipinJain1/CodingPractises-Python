# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 14:51:57 2021

https://leetcode.com/problems/single-number/submissions/

@author: VIP
"""

def singleNumber(nums):
     
     data = dict()
     for  i in nums:
         if i in data.keys():
             data[i] +=1
         else:
             data[i] =1
     for key, val in data.items():
         if val ==1:
             return key
         
    

nums = [4,1,2,1,2]
print (singleNumber(nums))