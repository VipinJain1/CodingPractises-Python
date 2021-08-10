# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 14:12:16 2021

@author: VIP
"""


def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    app = []
    org = []
    appprint  = 0
    orgprint = 0
    for i in apples:
        app .append (i+a)
    for j in oranges:
        org .append (j+b) 
    
    for  i in app:
        if (i >= s and  i <= t):
            appprint = appprint+1
        
    for  i in org:
        if (i >= s and  i <= t):
            orgprint = orgprint+1
    
    print (appprint)
    print (orgprint)


s = 7
t =11
a =5
b =15
apples = [-2,2,1]
oranges = [5,-6]
countApplesAndOranges(s, t, a, b, apples, oranges)
