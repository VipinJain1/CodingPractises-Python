# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 21:01:04 2021

@author: VIP
"""

def almostSorted(arr):
    
    toReverse  = False
    a = []
    l = len(arr)
    for i in range (l):
        count  =0
        start  =0
        end  =0
        swap = False
  
        if  arr[i] > arr[i+1]:
            start = i
            while  arr[i] > arr[i+1]:
                count  = count +1
              
                if i ==l-1:
                    return 
                
                i = i+1
                
            if count >1:
                end = i
                toReverse  = True

            
            if toReverse  ==  True:
                arr[start:end+1] = reversed ( arr[start:end+1] )
                print ( "reverse", start, end)
                
                  

             
      
     
a = [1, 5, 4, 3, 2, 6]
#   a = [2,3,5,4]
aSorted = almostSorted(a)
print (aSorted) 

