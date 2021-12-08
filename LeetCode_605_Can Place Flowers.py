# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 10:45:33 2021

@author: VIP
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ln = len (flowerbed)
        if ln ==0:
            return 0
        
        if ln ==1 and flowerbed[0] ==0:
            return True
        
        cnt =0
        if ln >=2 and flowerbed[0] ==0 and flowerbed[1] ==0:
            flowerbed[0] =1
            cnt +=1
                    
        if ln >=2 and flowerbed[ln-1] ==0 and flowerbed[ln-2] ==0:
            flowerbed[ln-1] =1
            cnt +=1
   
        start =1
        end  =  ln -1
        
        while (start <end):
            if flowerbed[start-1] ==0 and flowerbed[start] == 0 and flowerbed[start+1] ==0:
                cnt +=1
                flowerbed[start] =1
            start +=1
            
        return (cnt  >=n)
    
                
                
                
            
            
    
        