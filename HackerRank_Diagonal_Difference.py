# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 13:08:59 2021

@author: VIP
"""


arr = [
     [11, 2, 4], 
     [4, 5, 6], 
     [10, 8, -12]
   ]

sum1 =0
sum2 =0 
ln = len( arr[0]) -1
ln1 = ln
count  =0


while (count <=ln):
    sum1 = sum1 + arr[count][count]
    count = count +1
    
count =0
while (count <=ln and ln1 >=0):
    sum2 =  sum2 + arr [count][ln1]
    ln1 = ln1-1
    count = count +1

print ( abs ( sum1 - sum2))