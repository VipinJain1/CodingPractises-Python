# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 08:57:39 2021

https://www.hackerrank.com/challenges/compare-two-linked-lists/problem

@author: VIP
"""



def compare_lists(headA, headB):
    
    if (headA is None or headB is None):
        return 0
    else:
        nodeA = headA
        nodeB = headB
        flag = 1     
        while (nodeA is not None and nodeB is not None):
            if nodeA.data  != nodeB.data:
                flag = 0
                    
            nodeA  = nodeA.next
            nodeB = nodeB.next
        
        if flag == 0:
            return 0
        
        else:
            if (nodeA  is None and nodeB is not None ):
                return 0
                
            elif (nodeB  is None and nodeA is not None ):
                return 0         
            #else:
            #    return 1
            elif (nodeA  == None and nodeB == None ):
                return 1