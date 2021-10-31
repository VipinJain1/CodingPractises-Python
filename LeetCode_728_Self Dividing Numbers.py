# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 08:43:25 2021

@author: VIP
"""

class Solution:
 def isSelfDivNumber(self,num):
 n = str(num)
 if '0' in n:
 return False
 found = True
 for i in n:
 if num % int(i) !=0:
 found = False
 return found
 return found

 def selfDividingNumbers(self, left: int, right: int) -> List[int]:
 res = []
 for i in range (left, right+1):
 #print (i)
 if self.isSelfDivNumber(i):
 res.append(i)
 return res 
