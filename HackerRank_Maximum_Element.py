# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 22:51:27 2021

@author: VIP
"""



def getMax(operations):
    # Write your code here
    #print (operations)
    A  = []
    results = []
    for i in operations:
        data = i.split(' ')
        if data[0] == '1':
            A.extend(data[1:])
        elif  data[0] == '2':
            del A[len(A) -1]
        elif  data[0] == '3':
            results.append (max(A))
    return results
        
operations = ['1 97', '2', '1 20', '2', '1 26', '1 20', '2', '3', '1 91', '3']

print (getMax(operations))