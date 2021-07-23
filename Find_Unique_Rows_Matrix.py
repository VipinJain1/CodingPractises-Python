# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 07:33:24 2021

@author: VIP

https://www.geeksforgeeks.org/print-unique-rows/

Print unique rows in a given boolean matrix
Difficulty Level : Hard
Last Updated : 01 Jul, 2021
Given a binary matrix, print all unique rows of the given matrix. 

Example: 

Input:
        {0, 1, 0, 0, 1}
        {1, 0, 1, 1, 0}
        {0, 1, 0, 0, 1}
        {1, 1, 1, 0, 0}
Output:
    0 1 0 0 1 
    1 0 1 1 0 
    1 1 1 0 0 
    
"""

count =0

def FindUniqueRows(Matrix):
    global count
    ln = len(Matrix) 
    for i in range (0,ln):
        
        Flag = True
        
        for j in range(i+1, ln):
            
            if Matrix [i] == Matrix[j]:
                Flag = False
                break
                
        if Flag == True:
            count = count +1
    return count


Matrix = [
   
    [0,1,0,1,1],
    [0,1,0,1,1],
    [0,0,1,1,0],
    [0,0,1,1,0],
    
    ]


print (" Total Unique Rows are ", FindUniqueRows(Matrix))


