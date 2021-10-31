# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 08:44:50 2021

@author: VIP
"""

class Solution:
 def isPerfectSquare(self, num: int) -> bool:
 if num**(1/2) % 1 == 0:
 return True
 else: 
 return False
