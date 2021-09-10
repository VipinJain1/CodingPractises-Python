# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 18:07:55 2021

@author: VIP
"""

def interpret(command):
     l = len(command)
     if l<=1:
         return command
     
     if '()' in command:
         command = command.replace("()","o" )
     if '(al)' in command:
         command = command.replace("(al)","al" )
         
     return command 
 

command  = "G()(al)"

print (interpret(command))   
 
     
     