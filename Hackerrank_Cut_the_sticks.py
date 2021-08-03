# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 21:35:28 2021

@author: VIP
"""

arr = [1,2,3]

arr =[5, 4, 4, 2, 2, 8]
    
def cutTheSticks(arr):
    # Write your code here
    output = []
    ln = len(arr)
    mn = min(arr)
    if ln == 0:
        return 0
    
    while (ln):
       new_arr = []
       output.append (ln)
      
       for i in range (len (arr)): 
           mn = min(arr)
           if (arr[i] -mn) !=0:
               new_arr.append (arr[i] -mn)
       if sum (new_arr) ==0:
           break
       arr = new_arr
       ln = len (arr)
       if (sum (arr) == ln):
           output.append (ln)
           break
    return  output
        
        
print (cutTheSticks(arr))
 