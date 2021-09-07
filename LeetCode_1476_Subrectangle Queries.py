# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 17:05:47 2021

@author: VIP
"""

class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.matrix= copy.deepcopy(rectangle)
        
        if len(self.matrix)  ==0:
            return self.matrix
        

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for row in range (row1, row2+1):
            self.matrix[row][col1:col2+1] = [newValue] * (col2-col1+1)
        return self.matrix         
        

    def getValue(self, row: int, col: int) -> int:
        return self.matrix[row][col]
        


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)