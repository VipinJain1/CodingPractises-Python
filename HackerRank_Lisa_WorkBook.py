# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 11:54:58 2021

@author: VIP
"""


def workbook(n, k, arr):
    import math 
    # Write your code here
    special = 0
    page = 0
    earlierpage = 0
    for count, num in enumerate (arr):
        earlierpage = page
        page = page + math.ceil(num/k)
        count = 1
        for i in range (0,math.ceil(num/k)):
            if ((earlierpage + count  >= 0) and (earlierpage + count < k+k*i)):
                special+=1
                count +=k
                
    return special
            
        

#k =3
#n =5
#arr = [4,2,6,1,10]


n = 10
k= 5
arr = [3,8,15,11,14,1,9,2,24,31]
print (workbook(n, k, arr))

