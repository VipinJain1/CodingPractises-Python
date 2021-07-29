# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 19:23:23 2021

Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 203. Remove Linked List Elements


https://leetcode.com/problems/remove-linked-list-elements/submissions/

@author: VIP
"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        root = ListNode(0)
        root.next  = head
        head  = root
        current  = head
        
        while (root.next):
            
            if (root.next.val == val):
                root.next = root.next.next
            else:
                root = root.next
        #head = root       
        return head.next        
        
        