# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 01:36:09 2021

@author: VIP
"""

def largestNumber(nums):
    ln = len(nums)
    if ln ==0:
        return 0
    if ln ==1:
        return nums
    nums1 = sorted(nums)[::-1]
    s = str()
    dct ={}
    for i in nums1:
        dgt = int (str(i)[0])
        print (dgt)
        if dgt not in dct.keys():
            dct[dgt] = [i]
        else:
            dct[dgt].append(i)
    
    
    st = str()
    cnt =9
    while (cnt>=0):
        if cnt in dct.keys():
            st = st + "".join([str(elm) for elm in sorted(dct[cnt])[::-1]])
            cnt = cnt -1
        else:
            cnt = cnt-1
    return st    
        
        
nums = [3,30,34,6,9]
print (largestNumber(nums))