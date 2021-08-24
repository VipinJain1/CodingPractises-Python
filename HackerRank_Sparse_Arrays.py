# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 14:59:57 2021

https://www.hackerrank.com/challenges/sparse-arrays/problem

@author: VIP
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

def matchingStrings(strings, queries):
    # Write your code here
    
    strs  = dict()
    results = []
    
    for i in strings:
        if i in strs.keys():
            strs[i] +=1
        else:
           strs[i] =1
    
    for data in queries:
        if data in strs.keys():
            results.append (strs[data])
        else:
            results.append (0)
    return results      
     
        
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
