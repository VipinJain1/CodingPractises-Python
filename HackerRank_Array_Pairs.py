# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 13:39:44 2021

@author: VIP
"""


def solve(arr):
    count =0
    mx = 0
    for  i in range (len(arr)):
       
        for j in  range (i+1,len(arr)):
            mx = max(arr[i:j])
            if (i <j and (arr[i]*arr[j] <= mx)):
                count +=1
                
    return count


arr = [1, 1 ,2, 4, 2]    

print (solve(arr))    
    