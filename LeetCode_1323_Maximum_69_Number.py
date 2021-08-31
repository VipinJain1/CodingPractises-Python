# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 18:42:15 2021

@author: VIP
"""

def maximum69Number (num):
      
      if num <5:
          return num
      newstr = str()
      count =0
      found  = False
      for i in str(num):
          
          if i =='6' and found != True:
              newstr = newstr +'9'
              found = True
          else:
              newstr = newstr + i
      return int (newstr)
      
  

num  = 6
  
print (maximum69Number (num))
