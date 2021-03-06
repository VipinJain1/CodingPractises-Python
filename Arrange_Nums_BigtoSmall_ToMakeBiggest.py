# -*- coding: utf-8 
"""
Created on Wed Jul 21 13:58:18 2021

@author: VIP

https://www.geeksforgeeks.org/given-an-array-of-numbers-arrange-the-numbers-to-form-the-biggest-number/

Given an array of numbers, arrange them in a way that yields the largest value. For example, if the given numbers are {54, 546, 548, 60}, the arrangement 6054854654 gives the largest value. And if the given numbers are {1, 34, 3, 98, 9, 76, 45, 4}, then the arrangement 998764543431 gives the largest value.

Recommended: Please solve it on “PRACTICE ” first, before moving on to the solution. 
 
A simple solution that comes to our mind is to sort all numbers in descending order, but simply sorting doesn’t work. For example, 548 is greater than 60, but in output 60 comes before 548. As a second example, 98 is greater than 9, but 9 comes before 98 in output.

So how do we go about it? The idea is to use any comparison based sorting algorithm. 
In the used sorting algorithm, instead of using the default comparison, write a comparison function myCompare() and use it to sort numbers. 

Given two numbers X and Y, how should myCompare() decide which number to put first – we compare two numbers XY (Y appended at the end of X) and YX (X appended at the end of Y). If XY is larger, then X should come before Y in output, else Y should come before. For example, let X and Y be 542 and 60. To compare X and Y, we compare 54260 and 60542. Since 60542 is greater than 54260, we put Y first.

Following is the implementation of the above approach. 
To keep the code simple, numbers are considered as strings, the vector is used instead of a normal array. 



Below is the implementation of the above approach: 
    
"""

import random as rd

def arrangeNumsToMakeBiggest(nums):
    max = str()
    data =  dict()

    #print (ln)
    for i in nums:
        if  str(i)[0] in data:
            data[(str(i))[0]].append (i)
        else:
            data[(str(i))[0]] = [i]
   
    for i in range (9,-1,-1):
        
        if str(i) in data:
            for j in data [str(i)]:
                max = max + str(j)
                
           
    return max     
        
      

# Start Program from here

nums = rd.sample(range(0,1000), 12)

print ("Nums are ...", nums)
print (" Max Possible number is " ,arrangeNumsToMakeBiggest(nums))









