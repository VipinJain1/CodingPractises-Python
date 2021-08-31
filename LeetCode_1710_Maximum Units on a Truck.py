# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 13:28:55 2021

@author: VIP
"""

def maximumUnits( boxTypes, truckSize):
       d = {}
       
       for i in boxTypes:
           if i[1] in d.keys():
               d[i[1]] =  d[i[1]] + i[0]
           else:    
               d[i[1]] = i[0]
       
       maxVal  =0
       
       for i in sorted (d.keys())[::-1]:
           if truckSize >=0:
               if d[i] <= truckSize:
                   maxVal = maxVal + d[i] * i
                   truckSize = truckSize - d[i]
               else:
                   maxVal = maxVal + truckSize * i
                   truckSize = 0
                   
       return maxVal
           
           
#boxTypes = [[1,3],[2,2],[3,1]]
boxTypes = [[2,1],[4,4],[3,1],[4,1],[2,4],[3,4],[1,3],[4,3],[5,3],[5,3]]
truckSize = 13
print (maximumUnits(boxTypes, truckSize))

         