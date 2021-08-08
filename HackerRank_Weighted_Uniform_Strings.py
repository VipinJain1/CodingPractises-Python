# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 11:21:29 2021

@author: VIP
"""

def weightedUniformStrings(s, queries):
    
    ln =  len(s)
    
    data = []
    
    sct = dict()
    
  
    for i in range (1,len(s)):
        num =  int (ord(s[i-1]) -97)
        data.append(num)
        count  =1 
        while s[i-1] == s[i]:
            data.append()
            
         


queries = [5]
s = 'aaabbbbcccddd'

result = weightedUniformStrings(s, queries)
                       

