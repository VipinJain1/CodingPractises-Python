# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 16:10:15 2021
https://leetcode.com/problems/linked-list-cycle/submissions/

@author: VIP
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        if head == None or head.next == None:
            return False 
        
        root = head
        while (root):
            root = root.next
            head= head.next
            head = head.next
            if root == head:
                return True
            
            if root == None or root.next  == None:
                return False 
            if head == None or head.next  == None:
                return False 
        