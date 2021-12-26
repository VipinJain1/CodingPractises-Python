# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 14:40:10 2021

@author: VIP
"""
def frequency_sort(a):
    ln = len(a)
    if ln <=1:
        return a 
    d  = dict()
    for i  in a :
        if i  in d.keys():
            d[i] +=1
        else:
            d[i] =1

    import heapq
    
    l = list (d.items())
    
    result = []
    heapq.heapify(l)
    res  = heapq.nlargest(ln,l, lambda x: x[1])
    print (res) 
    
    from itertools import repeat
    
    
    for i in res:
        result.extend(repeat(i[0], i[1] ))
      
    return result 
# Program starts here
a = [1,1,2,3,4,5,5,66,2,3,4,1,2,3,4]
print (frequency_sort(a))