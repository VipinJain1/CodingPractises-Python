# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 07:10:32 2021

@author: VIP
"""



def findelem(a, start,end, num):
    
    if num == a[start]  or num == a[end]:
        return True
      
    mid  = int ((start+end)/2)
    
    if num == a[mid]:
        return True
    
    if (mid == start  or mid == end) and (num != a[start] or num != a[end]):
        return False
    
   
    if num >= a[mid] and num <= a[end]:
        findelem(a, mid,end,num)
    else:
        findelem(a, start,mid,num)
 
a = [7,8,9,1,1,1,1,2,2,3,4,5,6]
ln = len(a)
start = 0
num =12
end  = ln -1
print (findelem (a, start, end, num))