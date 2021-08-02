# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 18:08:07 2021

https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

@author: VIP
"""


x=2
y =3
z= 4

def catAndMouse(x,y,z):
    
    if  abs(z-x) > abs(z-y):
        return ("Cat B")
            
    if  abs(z-x) < abs(z-y):
        return ("Cat A")
    
    if  abs(z-x) ==  abs(z-y):
        return ("Mouse C")
        
        
catAndMouse(x,y,z)