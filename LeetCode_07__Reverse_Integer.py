# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 20:21:21 2021

7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321

@author: VIP
"""



class Solution:
    def reverse(self, x: int) -> int:
        minus = False
        lower = -2**31
        upper = 2**31 -1
        if x <0:
            x = abs(x)
            minus = True
        
        strnum = [v for v in str(x)][::-1]
        
        num = str()
        
        for i in strnum:
            num = num+ i
            
        realnum = int(num)
        
        if minus:
            realnum = 0 - realnum 
        
        if realnum > lower and realnum < upper:
            return realnum
        else:
            return 0
