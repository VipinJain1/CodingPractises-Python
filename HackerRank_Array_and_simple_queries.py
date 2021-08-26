# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 13:47:44 2021

@author: VIP
"""
import os

def arrayQueries(arr,queries ):

    first = arr[0]
    for query in queries:
        start = query[1] -1
        end = query[2]
        new =  arr[start:end]
        del arr[start:end]
        
        if query[0] ==1:
            new.extend (arr)
            arr = new
            #print (arr)
        else:
            arr.extend (new)
            #print (arr)
            
    last = arr[0]
    result =  dict()
    result[0] =  (abs(last - first))
    result[1] = arr
    print (result [0])
    print (result [1])
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayQueries(arr, queries)
    fptr.write(str(result[0]) + '\n')
    fptr.write(' '.join(map(str, result[1])))
    fptr.write('\n')
    fptr.close()
