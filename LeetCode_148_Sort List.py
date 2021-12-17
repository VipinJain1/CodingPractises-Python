# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        root = head
        root1 = head
        
        while (root):
            newroot = root.next
            while  (newroot):
                if root.val > newroot.val:
                    root.val, newroot.val = newroot.val, root.val 
                
                newroot = newroot.next
            root = root.next
        
        return root1
    