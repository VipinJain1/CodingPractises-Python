# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 13:40:25 2021

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

https://leetcode.com/problems/implement-strstr/
 

@author: VIP
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            ls = len(needle)
            ll = len(haystack)

            for i in range (ll-ls+1):
                if haystack[i:i+ls] == needle:
                    return( i)
        else:
            return (-1)
