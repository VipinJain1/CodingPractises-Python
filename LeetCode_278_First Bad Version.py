# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 22:09:20 2021

@author: VIP
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start =0
        end = n
        while (start <=end):
            mid  = (start+end)//2
            if isBadVersion(mid):
                #print (end)
                end = mid
            else:
                #print ("start", start)
                #print ("end", end)
                start = mid+1
            if start == end and isBadVersion(start):
                return start
                
                