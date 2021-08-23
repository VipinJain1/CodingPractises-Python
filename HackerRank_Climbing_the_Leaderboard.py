# -*- coding: utf-8 -*-
"""
Created
https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

@author: VIP
"""


def climbingLeaderboard(ranked, player):
    
    s =  set(ranked)
    ranked = list(s)
    ranked.sort(reverse = True)
    rank = []
    
    if len (ranked) ==0 or len (player) ==0:
        return None
    
    
    for p in player:
        count =1 
      
        found = False
        for r in ranked:
            if p <r:
                count +=1
            elif p ==r:
                rank.append(count)
                found = True
                break
            elif p >r:
                rank.append(count)
                found = True
                break
                
        if found == False:
            rank.append(count)
    return rank
                
        
            
  

ranked = [100,90,90,80]
player = [70,80,105]
ranked = [100,100,50,40,40,20,10]
player = [5,25,50,120]

ranked = []
player = [50,65,77,90,102]

print (climbingLeaderboard(ranked, player))