# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 10:36:36 2021

https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem

@author: VIP
"""


def printLinkedList(head):
    if head == None:
        return 0
    root = head
    while (root):
        print ( root.data)
        root = root.next