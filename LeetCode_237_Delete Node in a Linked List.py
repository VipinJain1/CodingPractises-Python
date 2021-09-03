# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 09:18:46 2021

@author: VIP
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
      
        n = node
        if n  == None:
            return
        n1 =  node.next
        n.val= n1.val
        p = n1
        n.next = n.next.next
        del p
        