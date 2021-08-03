# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 09:16:24 2021

@author: VIP

https://www.hackerrank.com/challenges/strong-password/problem

Louise joined a social networking site to stay in touch with her friends. The signup page required her to input a name and a password. However, the password must be strong. The website considers a password to be strong if it satisfies the following criteria:

Its length is at least .
It contains at least one digit.
It contains at least one lowercase English character.
It contains at least one uppercase English character.
It contains at least one special character. The special characters are: !@#$%^&*()-+
She typed a random string of length  in the password field but wasn't sure if it was strong. Given the string she typed, can you find the minimum number of characters she must add to make her password strong?

Note: Here's the set of types of characters in a form you can paste in your solution:
"""


    
import re 

n = 11
password  = '#HackerRank'
password =  'h%'
password  = 'AUzs-nV'


def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    
    numbers = '[0123456789]'
    lower_case = '[abcdefghijklmnopqrstuvwxyz]'
    upper_case = '[ABCDEFGHIJKLMNOPQRSTUVWXYZ]'
    special_characters = '[!@#$%^&*()-+]'
    newspecial_char =  '[-]'
    
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
    
    if  (newspecial  ==0 or special ==0) :
        special =0
    
    missing =  special + upper + lower + digit
    
    if ln + missing >=6:
        return  missing
    else:
        needed =  (6 - (ln+ missing))   + missing 
        return needed 
            
print (minimumNumber(n, password))