# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 14:04:39 2021

@author: VIP
"""
class Solution:
    def maximum69Number (self, num: int) -> int:
        
        if num <=5:
            return 0
        
        max =0
        cnt = 0
        ln = str(num)
        for i in str(num):
            if i ==6:
                return int (str[0:cnt] +'9' + str[i+1:ln])
                
                
            

            
        
                
num = 9669

print (maximum69Number(num))