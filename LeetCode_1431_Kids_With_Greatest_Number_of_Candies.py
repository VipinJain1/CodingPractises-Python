# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 16:48:45 2021

@author: VIP
"""

def kidsWithCandies(candies,extraCandies):
      l = len(candies)
      if  l== 0:
          return None
      result = []
      
      for count, i in enumerate (candies):
          if i + extraCandies >= max(candies):
              result.append (True)        

          else:
              result.append (False)  
      return result 
  
    
candies =  [2,3,5,1,3]
extraCandies =3
print (kidsWithCandies(candies,extraCandies))