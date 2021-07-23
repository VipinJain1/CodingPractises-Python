# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 11:04:08 2021

@author: VIP

https://www.geeksforgeeks.org/find-maximum-element-row-matrix/

Find maximum element of each row in a matrix
Difficulty Level : Basic
Last Updated : 08 Jun, 2021
Given a matrix, the task is to find the maximum element of each row.
Examples: 
 

Input :  [1, 2, 3]
         [1, 4, 9]
         [76, 34, 21]

Output :
3
9
76

Input : [1, 2, 3, 21]
        [12, 1, 65, 9]
        [1, 56, 34, 2]
Output :
21
65
56
"""

def findMaxElemRowWiseInMatrix(mat):
    for i in mat:
        print (max (i)) 

def findMaxElemRowWiseInMatrixNoLibFnUsage(mat):
    
    for i in mat:
        max = i[0]
        for j in i:
            if max < j:
                max =j
        print (max)
           
    
matrix = [
             [1,2,3],
             [2,3,4,8],
             [8,32,4,0]
         
         ]


# Find max element per row from Matrix using library function 
findMaxElemRowWiseInMatrix(matrix)

# Find max element per row from Matrix without library function 
findMaxElemRowWiseInMatrixNoLibFnUsage(matrix)