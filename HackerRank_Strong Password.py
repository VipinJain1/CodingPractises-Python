# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 09:16:24 2021

@author: VIP
"""

import re 
  
numbers = '[0123456789]'
lower_case = '[abcdefghijklmnopqrstuvwxyz]'
upper_case = '[ABCDEFGHIJKLMNOPQRSTUVWXYZ]'
special_characters = '[!@#$%^&*()-+]'
newspecial_char =  '[-]'


n = 11
password  = '#HackerRank'
password =  'h%'
password  = 'AUzs-nV'


def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    
    special = 0
    digit =0
    upper = 0 
    lower  =0
    newspecial =  0
    
    ln = len (password)
    specialchar_check= re.compile(special_characters)
    
    if (specialchar_check.search(password) == None):
        special =1
    
    
    newspecial_check = re.compile (newspecial_char)
    
    if (newspecial_check.search(password) == None):
        newspecial =1
    
    digit_check = re.compile(numbers) 
    
    if (digit_check.search(password) == None):
        digit =1
    
    upper_check= re.compile(upper_case) 
    
    if (upper_check.search(password) == None):
        upper =1
    
    lower_check= re.compile(lower_case) 
    
    if (lower_check.search(password) == None):
        lower =1
    
    #if  (newspecial  ==1 or special ==1) :
    #    special =0
    
    missing =  special + upper + lower + digit
    
    if ln + missing >=6:
        return  missing
    else:
        needed =  (6 - (ln+ missing))   + missing 
        return needed 
     
        
    
 
print (minimumNumber(n, password))