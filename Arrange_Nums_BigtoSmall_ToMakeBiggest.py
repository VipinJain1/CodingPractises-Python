# -*- coding: utf-8 
"""
Created on Wed Jul 21 13:58:18 2021

@author: VIP
"""

import random as rd

def arrangeNumsToMakeBiggest(nums):
    max = str()
    data =  dict()

    #print (ln)
    for i in nums:
        if  str(i)[0] in data:
            data[(str(i))[0]].append (i)
        else:
            data[(str(i))[0]] = [i]
   
    for i in range (9,-1,-1):
        
        if str(i) in data:
            for j in data [str(i)]:
                max = max + str(j)
                
           
    return max     
        
      

# Start Program from here

nums = rd.sample(range(0,1000), 12)

print ("Nums are ...", nums)
print (" Max Possible number is " ,arrangeNumsToMakeBiggest(nums))









