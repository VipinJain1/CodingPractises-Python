# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 11:40:15 2021

https://www.hackerrank.com/challenges/kaprekar-numbers/problem

@author: VIP
"""

def kaprekarNumbers(p, q):
    # Write your code here
    num0 = num1 =0
    Kaprekar_nums = []
    for i in range (p,q+1):
       
        st =  str (i**2)
        ln = len(st)
        if ln == 0:
            return 0
        if ln ==1:
            num0 =  int (i)
         
        if ln >=2:
            num0 =  int (st[0:int (ln/2)])
            num1 =  int (st[ln+1:ln])
           
        else:
            num1 = 0
        if ((num0 + num1) == i):
            Kaprekar_nums.append(i)
    
    return Kaprekar_nums

p =1
q =100
print (kaprekarNumbers(p, q))