# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 23:11:12 2021

@author: VIP
"""

def encryption(s):
    import math 
    # Write your code here
    s = s.replace(' ', '')

    numL = math.floor(math.sqrt(len(s)))
    numH = math.ceil(math.sqrt(len(s)))
    
    if ((numL*numH) <len(s)):
        numL = numL +1
    
    
    arr = []
    count = 0
    for i in range (0,numL):
        arr.append(s[count:count +numH])
        count = count + numH
    #print (arr)
    result = []
    count =0
    s = str()
    for i in range (0,numH):
        for j in arr:
            if j != None and len(j) > count:
                s = s+ j[count]
        count +=1
        if len(s) >=1:
            result.append(s)
        s = ''
    return result
  
s = 'haveaniceday'

result = encryption(s)
print (result)
