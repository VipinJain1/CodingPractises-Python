"""
Created on Thu Jul 22 07:33:24 2021

@author: VIP


https://www.geeksforgeeks.org/program-for-factorial-of-a-number/

Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n. For example factorial of 6 is 6*5*4*3*2*1 which is 720.
 
Recursive Solution: 
Factorial can be calculated using following recursive formula. 
 

  n! = n * (n-1)!
  n! = 1 if n = 0 or n = 1
  
"""

def fact(n):

    if  n ==0:
        return True

    return ( n * fact(n-1))

n = int (input (" Enter Nmmber:" ))
print ( "n === ", n)
print (fact(n))