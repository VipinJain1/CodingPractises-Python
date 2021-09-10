# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 17:34:49 2021

@author: VIP
"""

def getDecimalValue(self, head: ListNode) -> int:
       l = []
       root = head
       cnt  =0
       dec =0
       while (root):
           l.append(root.val)
           root= root.next
       for i in l[::-1]:
           dec = dec + i* 2**cnt
           cnt +=1
           
       return dec    
   

l = 