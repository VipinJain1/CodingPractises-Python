# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 08:31:52 2021
https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse/problem

@author: VIP
"""


def reversePrint(llist):
    # Write your code here
    
    l = []
    head = llist
    if head == None:
        print (None)
    while (head):
        l.append(head.data)
        head = head.next
    ln = len(l) -1
    for i in l:
        print (l[ln])
        ln = ln-1