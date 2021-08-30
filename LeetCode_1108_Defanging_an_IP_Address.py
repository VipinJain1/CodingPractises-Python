# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 13:33:06 2021

@author: VIP
"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        if len (address)  == 0:
            return None
        
        address= address.replace('.', '[.]')
        return address