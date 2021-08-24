# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 09:00:15 2021

https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list/problem

@author: VIP
"""


def removeDuplicates(llist):
    # Write your code here
    
    head = llist
    root1 = llist
    
    root2  =  llist.next
    
    while root1 != None or root2 != None:
        
        if root1.next == None:
            return head
        if root1.data == root2.data:
            root1.next = root1.next.next
            root2 = root1.next
        else:
            root1 = root1.next
            root2  = root2.next
    return head