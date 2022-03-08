# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 18:39:24 2022

@author: VipLeo
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        lnx  = len(matrix)
        lny  = len(matrix[0])
        if lnx ==0: 
            return None
        
        if lnx ==1 and 0 in matrix[0]:
            matrix[0] = [0]* lny
            return matrix 
        
        zeroset = set()
        for x in range(lnx):
            for y in range (lny):
                if matrix[x][y] ==0:
                    zeroset.add((x,y))
        if len(zeroset) >0:
            for x1,y1 in zeroset:
                for i in range (lnx):
                    matrix[i][y1] =0
                for i in range (lny):
                    matrix[x1][i] =0
                 
        return matrix
                
            
            