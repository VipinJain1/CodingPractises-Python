# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 12:24:22 2021
https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem

@author: VIP
"""


def findMergeNode(head1, head2):
    root1 = head1
    root2 = head2
    root11 = head1
    root22 = head2
    
    if root1 is None or root2 is None:
        return False
    
    while (root1):
        while (root2):
            root2 = root2.next
            if root1 == root2:
                return root1.data
        root2 = root22    
        root1 = root1.next
            
             