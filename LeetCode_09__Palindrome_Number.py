<<<<<<< HEAD
export PATH=$PATH:"C:\VipDevelopment\CodingPractises\CodingPractises-Python"
=======
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 16:18:04 2021

9. Palindrome Number
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

@author: VIP
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        v = [i for i in str(x)]
        return v == v[::-1]   
        