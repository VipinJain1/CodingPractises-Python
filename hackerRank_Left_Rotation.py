# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 12:27:25 2021

@author: VIP
"""

def rotateLeft(d, arr):
    # Write your code here
    partial = arr[0:d]
    arr = arr[d:len(arr)]
    arr.extend(partial)
    return arr
    