# -*- coding: utf-8 -*-
"""

66. Plus One
Created on Thu Jul 29 23:56:51 2021

Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

 
https://leetcode.com/problems/plus-one/

@author: VIP
"""

digits = [9,8,9]

l = len(digits) -1
if l==1:
    digits[0]= digits[0] +1
    
carry =0

while (l >=0):
    if (digits[l] +1 == 10):
        digits[l] =0
        carry =1
        l = l-1
    else:
        if carry:
            digits[l] = digits[l] +  carry
        else:
            digits[l] = digits[l] +  carry
    else:
        break
        
print (digits)