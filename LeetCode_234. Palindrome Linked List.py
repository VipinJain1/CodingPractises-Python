# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 23:22:39 2021

https://leetcode.com/problems/palindrome-linked-list/

@author: VIP
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        root = head
        if root == None:
            return False
        l =[]
        while (root != None):
            l.append(root.val)
            root = root.next
        print (l)
        if l == l [::-1]:
            return True
        else:
            return False 
            
        
        