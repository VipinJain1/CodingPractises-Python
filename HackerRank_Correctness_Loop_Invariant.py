# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 22:02:25 2021

@author: VIP
"""


def insertion_sort(l):
    for i in range(0, len(l)): # 1 TO n
        for k in range(i+1, len(l)):
            if l[k] < l[i]:
                l[k],l[i] = l[i], l[k]
                

ar =  [7, 4, 3, 5, 6, 2]
            
insertion_sort(ar)
print (ar)
            
