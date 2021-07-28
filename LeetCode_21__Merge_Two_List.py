# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 16:18:04 2021

21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

 

@author: VIP
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = head = ListNode(0)
        
        while (l1 and l2):
            if (l1.val < l2.val):
                l3.next = l1
                l1 = l1.next
                l3 = l3.next
            else:
                l3.next = l2
                l2  =l2.next
                l3 = l3.next
            
        while (l1 and l2 is None):
                l3.next = l1
                l1 = l1.next
                l3 = l3.next
        while (l2 and l1 is None):
                l3.next = l2
                l2  =l2.next
                l3 = l3.next
                
        return head.next