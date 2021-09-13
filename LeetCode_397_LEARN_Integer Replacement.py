# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 09:35:21 2021

@author: VIP
"""
"""
def integerReplacement(n: int) -> int:
      if n == 1:
          return 0
      
      if n & 1:
          return 1 + min(integerReplacement(n-1), integerReplacement(n+1))
      else:
          return 1 + integerReplacement(n//2)
"""
   
from collections import deque 
  
def integerReplacement(n: int) -> int:
    queue = deque([n])
    seen  = set()
    seen.add(n)
    ans =0
    while (queue):
        for _ in  range (len(queue)):
            cur = queue.popleft()
            
            if cur ==1:
                return ans
        
            # odd number
            if cur %2:
                if cur+1 not in seen:
                    queue.append(cur+1)
                    seen.add(cur+1)
                    
                if cur-1 not in seen:
                    queue.append(cur-1)
                    seen.add(cur-1)
            else:
                if cur //2 not in seen:
                    queue.append(cur //2)
                    seen.add (cur//2)
        ans +=1
        
    return ans                     
      
n = 19
print (integerReplacement(n))    