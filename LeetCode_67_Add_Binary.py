# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 14:02:25 2021

@author: VIP
"""

def addBinary(a, b):
       
       if a == None and b != None:
           return b
       elif a != None and b == None:
           return a
       if a == None and b == None:
           return None
       
       result = str()
       carry = 0
       bl  = len(b) -1
       
       for i in (a[::-1]):

           if i =='1' and b[bl] =='1' and carry ==1 and bl >=0:
               carry =1
               result = result + '1' 
           elif i =='1' and b[bl] =='1'and carry ==0 and bl >=0:
               carry =1
               result = result + '0' 
           elif (i =='1' and b[bl] =='0') or (i =='0' and b[bl] =='1' ) and carry ==0 and bl >=0:
               carry =0
               result = result + '1' 
           elif (i =='1' and b[bl] =='0') or (i =='0' and b[bl] =='1' ) and carry ==1 and bl >=0:
               carry =1
               result = result + '0'
           
           elif  (i =='0' and b[bl] =='0')  and carry ==1 and bl >=0:
               carry =0
               result = result + '1'
           elif  (i =='0' and b[bl] =='0')  and carry ==0 and bl >=0:
               carry =0
               result = result + '0'
                
           elif bl <0:
               if carry:
                   if carry ==1 and i =='1':
                       result = result + '0'
                       carry =1
                   elif carry ==1 and i =='0':
                       result = result + '1'
                       carry =0
                   elif carry == 0 and i =='0':
                       result = result + '0'
                       carry  =0
                   elif carry == 0 and i =='1':
                       result = result + '1'
                       carry  =0
                      
                         
           bl = bl-1
       if carry ==1:
           result  = result + '1'
       return result [::-1]

a = "1"
b = "111"

print (addBinary(a, b))