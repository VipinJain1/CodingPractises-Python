# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 13:51:16 2021

@author: VIP
"""

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        ln = len(letters)
        if ln ==0:
            return None
        char = target
        found = False
        while (char <'z'):
            char = chr(ord(char) +1)
            if char in letters:
                found = True
                return char
        if found == False:
            return letters[0]
     
            
            
        
        
        