# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 10:41:24 2021

@author: VIP
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        root1 = headA
        d = {}
        root2 = headB
        while (root2):
            d[root2] =1
            root2 = root2.next
        while (root1):
            if root1 in d.keys():
                return root1
            root1 =root1.next
        return None