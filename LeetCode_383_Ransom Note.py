# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 08:37:21 2021

@author: VIP
"""

class Solution:
 def canConstruct(self, ransomNote: str, magazine: str) -> bool:
     d1 ={}
     d2 ={}
     for i in ransomNote:
         if i in d1.keys():
             d1[i] +=1
         else:
             d1[i] =1
     for i in magazine:
         if i in d2.keys():
             d2[i] +=1
         else:
            d2[i] =1

     flag = True
     for key, val in d1.items():
         if key not in d2.keys():
             flag = False
             return flag
         elif d1[key] > d2[key]:
             flag = False
             return flag
         else:
             flag = True
     return flag
    
obj  = Solution()
ransomNote ='aabaxx'
magazine = 'aabdaxxxxxxxxxxxxxx'
print (obj.canConstruct(ransomNote,magazine))