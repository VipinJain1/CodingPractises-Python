# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 08:37:19 2021

@author: VIP
"""

class Solution:
 def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

 d = dict()
 for i in strs:

 data= "".join(sorted(i))
 if data in d.keys():
 d[data] += [i] 
 else:
 d[data] =[i]
 print (d)
 res=[]
 for i, val in d.items():
 res.append (val)
 return res

Sent with a Spark
