# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 15:01:11 2021
https://www.hackerrank.com/challenges/the-hurdle-race/problem


A video player plays a game in which the character competes in a hurdle race. 
Hurdles are of varying heights, and the characters have a maximum height they can jump. There is a magic potion they can take that will increase their maximum jump height by  unit for each dose. How many doses of the potion must the character take to be able to jump all of the hurdles. If the character can already clear all of the hurdles, return .

@author: VIP
"""

k =4
height = [1 ,6, 3, 5, 2]
 

def hurdleRace(k, height):
    # Write your code here
    
    mx = max (height)
    if mx -k >0:
        return mx - k
    else:
        return 0


print (hurdleRace(k,height))


