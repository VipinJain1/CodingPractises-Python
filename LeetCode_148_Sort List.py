# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 14:05:48 2021

@author: VIP
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        root  = head
        if root == None:
            return head
        
        root1 = root
        
        while (root1 != None):
            root = head
            while (root != None):
                if root.next != None:
                    if root.val > root.next.val:
                        root.val, root.next.val = root.next.val, root.val
                root = root.next
            root1 = root1.next
            
        return head
                
                
        
        
        