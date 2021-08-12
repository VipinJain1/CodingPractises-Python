# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 08:32:51 2021

https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem

@author: VIP
"""


# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def has_cycle(head):
    root = head
    root1 = head.next
    
    if root == None or root.next ==  None or root.next.next == None:
        return 0
    
    while (root and root1):
        if root == root1:
            return 1
        
        if root1.next == None:
            return  0
        else:
            root = root.next
        
        if root1.next == None or root1.next.next == None:
            return 0
            
        else:
            root1 = root1.next.next
        
        if root == None or root.next ==  None:
            return 0
        
        
        
        
        
        
        
        