# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 11:28:46 2021

https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem

@author: VIP
"""


def insertNodeAtPosition(llist, data, position):
    # Write your code here
    if llist is None:
        return 0
    
    count  = 1
    root = llist
    head = llist
    
    while (root):
        if count == position:
            node = SinglyLinkedListNode(data)
            pntr =  root.next
            root.next = node
            node.next =  pntr
               
        count  += 1
        root = root.next
    return head
    