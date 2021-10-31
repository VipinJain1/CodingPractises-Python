# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 09:07:59 2021

@author: VIP
"""

class Solution:
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        d1 = {}
        d2 ={}
        d3 ={}
        for i in arr1:
            if i in d1.keys():
                d1[i] +=1
            else:
                d1[i] = 1
        
        for i in arr2:
            if i in d2.keys():
                d2[i] +=1
            else:
                d2[i] = 1
        
        
        for i in arr3:
            if i in d3.keys():
                d3[i] +=1
            else:
                d3[i] = 1
        res =[]
        for i in arr1:
            try:
                data = min (d1[i], d2[i], d3[i])
                res.extend([i]*data)
            except:
                continue
        return res        
            
obj = Solution()
arr1 = [1,2,3,4,5]
arr2 = [1,2,3,4,5]
arr3 =[1,6]

print (obj.arraysIntersection(arr1,arr2,arr3))          