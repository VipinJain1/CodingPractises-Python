# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 18:08:07 2021

https://www.hackerrank.com/challenges/library-fine/problem

@author: VIP
"""

# Actual Retunred date
d1 = 9
m1 = 6 
y1 = 2015

# Actual Due Date with no Fine 
d2= 6 
m2= 6 
y2= 2015

def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here

   if  (y1 > y2):
       return 10000
   elif  ((m1 >m2) and (y1==y2)):
       return ((m1-m2 ) * 500)
   elif ((d1>d2) and  (m1 == m2) and (y1 ==y2)):
       return ((d1-d2) *15)
   
    # book returned on time
   elif ((d2 > d1) and (m1 == m2) and (y1 ==y2)):
       return 0
   else:
       return 0

print (libraryFine (d1, m1, y1, d2, m2, y2))
