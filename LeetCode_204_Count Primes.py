# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 21:58:28 2021

@author: VIP
""" 

def createTargetArray(nums, index):
        
        ln1 = len(nums)
        ln2 = len (index)

        if ln1 ==0 or ln2 ==0:
            return None
        res  = [] 
        cnt  =0
        for i in nums:
            res.insert(index[cnt],i)
            cnt +=1
        return res            

nums = [0,1,2,3,4]
index = [0,1,2,2,1]
 
print (createTargetArray(nums,index))