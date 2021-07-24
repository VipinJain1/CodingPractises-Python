# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 14:47:48 2021

Find the minimum element in a sorted and rotated array
Difficulty Level : Medium
Last Updated : 01 Apr, 2021
A sorted array is rotated at some unknown point, find the minimum element in it. 
The following solution assumes that all elements are distinct.

https://www.geeksforgeeks.org/find-minimum-element-in-a-sorted-and-rotated-array/

Examples: 

Input: {5, 6, 1, 2, 3, 4}
Output: 1

Input: {1, 2, 3, 4}
Output: 1

Input: {2, 1}
Output: 1

@author: VIP

"""

def getMin(data,mid, start,end):
    
    if len(data[start:end]) == 1 :
        return data[start]
        
    
    if len(data[start:end]) == 2:
        if data[start] < data[end]:
            return data[start]
        else:
            return data[end]
    
    if ((data[mid] >  data[mid-1] ) 
        and (data[start] > data[end]) 
        and data[mid] < data[mid+1] 
        and data[mid])> data[end]:
        
        #min is i  left array
        start = mid
        end = end
        mid =  int ((start+end)/2)
        #data = data[start:end]
        return getMin(data, mid, start,end)
    else:
        
        #min is in right array
        start = start
        end = mid+1
        mid = int ((start + mid)/2)
        #data = data[start:end]
        return getMin(data, mid, start,end)

def FindMin(data):
    mid = int (len(data)/2)
    end = (len(data)) -1
    start = 0   
    val = getMin(data,mid,start,end)
    return val
    

# Input
import random as rd
numOfElem = 20

data =  sorted(rd.sample (range (1,880),numOfElem))
print ("ONLY Sorted Data is        == ", data)

# get random number to move element by that number
movebysize= rd.randint(1,20)
print ("Move Sorted data by size   == ", movebysize)


# Make array rotated
data = data[movebysize:] + data[:movebysize]
print ("Data Sorted and Rotated is == ", data)

# Find Min:
#data = [[36, 39, 1, 4, 5, 8, 11, 12]]
print (" Min is ==== ", FindMin(data))

