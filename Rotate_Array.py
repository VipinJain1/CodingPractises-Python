# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 13:42:57 2021

Array Rotations

@author: VIP
"""

import random

# Rotate the list with same extra size of List.
def rotateArrayWithExtraSpace(lst,num):
    newList = []
    newList = lst[num:]
    ln = len(newList)
 
    for i in range(0,num):
        newList.append (lst[i]) 
        
    return newList


# Roate the list in Place
def rotateInPlace(lst,num):
    
    for i in range (0,num):
        tmp = lst[0]
        lst = lst[1:]
        lst.append(tmp)
    
    return lst
            
# Roate the list in Place in chunks
def rotateInPlaceChunkWise(lst,num):
    tmp = lst[:num]
    lst = lst[num:]
    lst = lst +tmp
    return lst
            

# Start Program from here
A = list()
for i in  range (0,10):
    A.append(i)
    
print ("List before Rotation", A)
n = random.randint(0,5)
print ("Rotate List by %d number of Elements" % n)
# rotae array by number of elements, create extra space 

print (rotateArrayWithExtraSpace(A,n))

B = list()
for i in  range (0,10):
    B.append(i)
    
print ("List before in place Rotation", B)
print ("List after  inplace  Rotation", rotateInPlace(B,n))


C = list()
for i in  range (0,10):
    C.append(i)
    
print ("List before in place ChunkWise rotation", C)
print ("List after  in place ChunkWise Rotation", rotateInPlaceChunkWise(C,n))
