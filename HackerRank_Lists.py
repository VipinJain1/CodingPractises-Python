# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 09:37:55 2021

@author: VIP
"""

myDict = {0: 'insert 0 5', 1: 'insert 1 10', 2: 'insert 0 6', 3: 'print', 4: 'remove 6', 
           5: 'append 9', 6: 'append 1', 7: 'sort', 8: 'print', 9: 
               'pop', 10: 'reverse', 11: 'print'}


lst  =list()
N = 11

for val in myDict.values():
    
    data = val.split (' ')
    if (data[0] == 'print'):
        print (lst)
    
    if data[0]  == 'insert':
        lst.insert(int (data[1]), int (data[2]))
    if data[0]  == 'remove':
        lst.remove(int (data[1]))
    if data[0]  == 'append':
        lst.append(int (data[1]))
    if data[0]  == 'sort':
        lst.sort()
    if data[0]  == 'pop':
        lst.pop()
    if data[0]  == 'reverse':
        lst = lst[::-1]
   

        
         
