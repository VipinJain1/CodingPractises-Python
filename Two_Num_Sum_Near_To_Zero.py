# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 14:47:48 2021

Two elements whose sum is closest to zero
Question: An Array of integers is given, both +ve and -ve. You need to find the two elements such that their sum is closest to zero.
For the below array, program should print -80 and 85.

Recommended: Please solve it on “PRACTICE” first, before moving on to the solution.
https://www.geeksforgeeks.org/two-elements-whose-sum-is-closest-to-zero/

@author: VIP
"""

# Time taken O(N2),  
def Find2Nums_SumClose2Zero(ip):
    
    bestVal =0
    minDist = ip[1]
    bestnum1  =0
    bestnum2 = 0
    for i in  range (0,len(ip)):
        for j in range (i+1,len(ip)):
           if abs (minDist) > abs ((ip[i] + ip[j])):
               minDist = ip[i] + ip[j]
               bestnum1 = ip[i]
               bestnum2= ip[j]
                
    return  bestnum1,  bestnum2      
        
        
import random as rd
InputData = rd.sample(range (-1666,300),30)
print ("Test data is ", InputData)
print ("Nunmbers are" , Find2Nums_SumClose2Zero(InputData))





