# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 10:50:20 2021

https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem

@author: VIP
"""


def getNode(llist, positionFromTail):
    # Write your code here
    
    if llist is None:
        return 0
    count =  0
    head = llist
    root = llist 
    while (head):
        count  += 1
        head = head.next
    pos = count - positionFromTail
    
    if pos <0:
        return 0
    
    newcnt =1 
    while ( root):
        if newcnt ==  pos:
            return ( root.data)
        root = root.next
        newcnt +=1
        