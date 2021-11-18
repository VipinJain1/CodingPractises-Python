# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 16:44:15 2021

@author: VIP
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        root = head
        if root == None or root.next == None:
            return head
        while (root.next != None):
            if root.val == root.next.val:
                root.next = root.next.next
            else:
                root = root.next
                
       
        return head   