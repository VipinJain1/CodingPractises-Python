# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 12:39:31 2021

@author: VIP
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        curr = head
        old2copy = {None:None}
        
        # Copy all the nodes into dict and point to copied nodes.
        while (curr):
            copy = Node(curr.val)
            old2copy[curr] = copy
            curr= curr.next
        
        # Visit all the original noded and point to next and random nodes for each one by one 
        curr = head
        while(curr):
            copy = old2copy[curr]
            copy.next = old2copy[curr.next]
            copy.random = old2copy[curr.random]
            curr = curr.next
        
        curr = head
        return old2copy[curr]
    
        
            
            