# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 15:41:46 2021

@author: VIP
"""



def restoreString(s, indices):
        ln = len(s)
        if ln ==0:
            return None
        
        if len(indices) ==0:
            return None
        count =0
        s1 = list (s)
        for i in indices:
            s1[count], s1[i] = s1[i], s1[count]
            count = count +1
        return s1 
    

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print (restoreString(s, indices))