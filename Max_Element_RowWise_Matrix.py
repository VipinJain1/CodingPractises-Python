# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 11:04:08 2021

@author: VIP
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