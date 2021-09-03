# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 13:34:42 2021

@author: VIP
"""

#DID NOT WORK YET

class Solution:
    def myAtoi(self, s: str) -> int:
        ln = len (s)
        s = s.strip()
        
        
        if ln ==0:
            return 0
        if ln ==1 and s[0].isnumeric() == False :
            return  0
            
        if ((s[0] == '-' and s[1] == "+" ) or (s[0] == '+' and s[1] =="-")):
            return  0
        
        if s[0] == '+':
            s = s[1:]
        
        if (s[0].isnumeric() == False  and s[0] != '-'):
            return 0
        
      
        num = 0
        minus = False
       
        if s[0] == '-':
            minus = True
            s = s[1:]
        
        for i in s:
            if i.isnumeric():
                num = num* 10 + int (i)
            else:
                break
            
        
        if minus:
            num = -num
        if num < -2**31:
            num = -2147483648
        if num > 2**31 -1:
            num = 2147483647

        return num   
                
            
        
                


s = "+-12"       
print (myAtoi(s))

