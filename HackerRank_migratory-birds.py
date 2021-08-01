# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 11:27:51 2021
https://www.hackerrank.com/challenges/migratory-birds/problem

Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type. If more than 1 type has been spotted that maximum amount, return the smallest of their ids.
Example

Example

There are two each of types  and , and one sighting of type . Pick the lower of the two types seen twice: type .

Function Description

Complete the migratoryBirds function in the editor below.

migratoryBirds has the following parameter(s):

int arr[n]: the types of birds sighted

@author: VIP
"""


def migratoryBirds(arr):
    # Write your code here
    bird = dict()
    if len (arr) ==0:
        return 0
    if len (arr) ==1:
        return arr[0]
    for i in arr:
        if i in bird.keys():
            bird [i] =  bird [i]+1
        else:
            bird[i] =1
    
    val = (max (bird.values()))
    #print (val)
    toReturn = []
    for key, value in bird.items():
         if value == val:
              toReturn.append(key)
    return min (toReturn)          
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

