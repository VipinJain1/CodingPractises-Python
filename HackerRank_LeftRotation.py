# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 17:32:38 2021

https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
@author: VIP
"""
def rotLeft(a, d):

def rotLeft(a, d):
    # Write your code here
    ln = len(a)
    if ln <=1 or ln ==d:
        return a
    if d>ln:
        d = d -ln
    
    return a[d:ln] + a[0:d]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()