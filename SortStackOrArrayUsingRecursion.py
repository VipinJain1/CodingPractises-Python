# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 15:14:14 2021

Sort stack uisng Recursion

@author: VIP
"""

def insertStack(data,temp):
    ln = len(data)
    if ln ==0 or data[-1] < temp:
        data.append(temp)
        return
    val = data.pop()
    insertStack(data,temp)
    data.append(val)
    
def sortStack(data):
    ln = len(data)
    if ln ==0:
        return 
    temp = data.pop()
    sortStack(data)
    insertStack(data,temp)

# data to store into list
stackdata = [9,0,1,2,3,56,0,6,-1,6]
sortStack(stackdata)
print (stackdata)