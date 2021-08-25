# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 21:40:37 2021

@author: VIP
"""
import heapq
  
def cookies(k, A):
    # Write your code here
    import heapq
    val = 0 
    heapq.heapify(A)
    
    count = 0  
   
    while ( True):
        
        if all ( y > k for y in A):
            return count
        
        count += 1
        val = 1* heapq.heappop(A) + 2* heapq.heappop(A)
        heapq.heappush(A,val)
        
        if len (A) ==0:
           return  -1
        if len (A) ==1 and A[0] < k:
           return -1 

k  = 7
A = [1,2,3,9,10,12]

print(cookies(k, A))