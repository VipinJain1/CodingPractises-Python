# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 09:01:43 2021

@author: VIP
"""


def reverse(llist):
    # Write your code here
    tail = llist
    t = llist
    head = llist
    
    tail = None
    while (head != None):
        t = head.next
        head.next = tail
        tail = head
        head = t
    
    return tail;
        