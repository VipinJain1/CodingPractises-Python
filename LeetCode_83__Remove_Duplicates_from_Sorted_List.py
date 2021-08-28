# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 23:11:16 2021

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
        while (root != None and root.next !=None):
            if root.val == root.next.val:
                root.next = root.next.next
            else:
                root = root.next
        return head