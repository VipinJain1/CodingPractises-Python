# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 01:36:09 2021

@author: VIP
"""

def largestNumber(A):
    ln = len(nums)
    if ln ==0:
        return 0
    if ln ==1:
        return str(nums[0])
    if all([ v == 0 for v in nums ]):
        return "0"
        
    dct ={}
    for i in nums:
        dgt = int (str(i)[0])

        if dgt not in dct.keys():
            dct[dgt] = [i]
        else:
            dct[dgt].append(i)


    st = str()
    cnt =9
    while (cnt>=0):
        if cnt in dct.keys():
            data = sorted(list (map(str,dct[cnt])))[::-1]
            if len(data) >=2:
                for i in range (0, len(data) -1):
                    if int(data[i] + data[i+1]) <  int(data[i+1] + data[i]):
                        data[i],data[i+1] = data[i+1], data[i]

            lst = "".join([elm for elm in data])
            st = st + lst
            cnt = cnt -1
        else:
            cnt = cnt-1
    return st    

nums = [3,30,34,6,9]
nums  = [10]
print (largestNumber(nums))