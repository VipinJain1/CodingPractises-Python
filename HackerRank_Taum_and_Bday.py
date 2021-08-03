# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 11:48:21 2021


https://www.hackerrank.com/challenges/taum-and-bday/problem

Taum is planning to celebrate the birthday of his friend, Diksha. There are two types of gifts that Diksha wants from Taum: one is black and the other is white. To make her happy, Taum has to buy  black gifts and  white gifts.

The cost of each black gift is  units.
The cost of every white gift is  units.
The cost to convert a black gift into white gift or vice versa is  units.
Determine the minimum cost of Diksha's gifts.

@author: VIP
"""

b  = 3
w  = 3
bc = 1
wc = 9
z  = 2

def taumBday(b, w, bc, wc, z):
    # Write your code here
    minCost = 0
    
    total_cost = b*bc + w *wc
    altcost1 = (wc+z)* b + wc*w
    altcost2 = (bc)* b + (bc+z)*w
    minCost = min (total_cost,altcost1,altcost2)     
    
    return minCost

print (taumBday(b, w, bc, wc, z))




