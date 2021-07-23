"""


Smallest subarray with all occurrences of a most frequent element
Difficulty Level : Medium
Last Updated : 21 May, 2021
Given an array, A. Let x be an element in the array. x has the maximum frequency in the array. Find the smallest subsegment of the array which also has x as the maximum frequency element.
Examples: 
 

Input :  arr[] = {4, 1, 1, 2, 2, 1, 3, 3} 
Output :   1, 1, 2, 2, 1
The most frequent element is 1. The smallest
subarray that has all occurrences of it is
1 1 2 2 1

Input :  A[] = {1, 2, 2, 3, 1}
Output : 2, 2
Note that there are two elements that appear
two times, 1 and 2. The smallest window for
1 is whole array and smallest window for 2 is
{2, 2}. Since window for 2 is smaller, this is
our output.
"""

def getmaxrepeatedNum(a):
    
    n ={}
    for i in a:
        if i in n:
            n[i] = n[i] +1
        else:
            n[i] = 1
       
    return n 
      
def maxrepeated (a):
    n= getmaxrepeatedNum(a)
    print (n)
    
    val = max(n.values())
    s = a.index(val)
    e= a[::-1].index(val)
    e = len(a) -3
    
    return a[s:e]
    
    
a = [91,2,3,4,5,5,6,5,5,6,5,6,7,8]

print (maxrepeated (a))