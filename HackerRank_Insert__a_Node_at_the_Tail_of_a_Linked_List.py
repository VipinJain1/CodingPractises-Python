# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 08:56:00 2021

https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem

@author: VIP
"""


def insertNodeAtTail(head, data):
    root = head
     
    if head  == None:
        node =  SinglyLinkedListNode(data)
        head = node
        return head
    
    while (root.next != None):
        root = root.next
    
    node =  SinglyLinkedListNode(data)
    root.next =  node
    node.next = None    
    return head 
