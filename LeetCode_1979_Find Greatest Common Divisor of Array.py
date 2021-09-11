# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 10:17:03 2021

@author: VIP
"""

def findGCD(nums):
       ln = len (nums)
       if ln ==0:
           return 0
       mn, mx = min(nums), max(nums)
       largest =0
       for i  in range (1, mx):
           if mn % i == 0 and mx %i ==0:
               if largest <i:
                   largest =i
                   
       return largest    


nums  = [3,3]

print (findGCD(nums))