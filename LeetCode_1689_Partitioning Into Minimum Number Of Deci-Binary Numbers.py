# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 12:40:29 2021

@author: VIP
"""

def minPartitions(n):
    answer = 0
    str = n

    while (int(str) > 0):
        str_list = []
        for i in range(len(str)):
            if str[i] > '0':
                str_list.append(chr(ord(str[i])-1))
    
        str = ''.join(str_list)
        answer += 1

    return answer


n = "0"

print (minPartitions(n))