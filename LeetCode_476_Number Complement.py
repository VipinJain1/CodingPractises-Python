# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 22:19:42 2021

@author: VIP
"""

class Solution:
    def findComplement(self, num: int) -> int:
        
        num = list(bin(num))[2:]
        res = []
    
        for  i in num:
            if i =='1':
                res.append('0')
            else:
                res.append('1')
                
            
        res = ('0b'+"".join(res))
        return  int(res,2)
    
        