# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 08:42:36 2021

@author: VIP
"""

def nearestGreator2Right(nums):
    ln = len(nums)
    if ln ==0:
        return None
    if ln ==1:
        return -1
    result =[]
    stack =[]
    result.append(-1)
    stack.append(nums[ln-1])
    for i in range (ln-2,-1,-1):
        if nums[i] < stack[len(stack)-1]:
            result.append(nums[i+1])
        else :
            if len (stack) >0:
                while nums[i] > stack[len(stack)-1]:
                    val = stack.pop()
                    if len(stack) >0:
                        continue
                    else:
                        break
                    
                if len(stack) ==0:
                    result.append(-1)
                else:
                    result.append(stack [len(stack)-1])
        stack.append(nums[i])
    return result 
    
arr = [1,2,34,1,9,7,4,9,2]
res = nearestGreator2Right(arr)
print (res[::-1])