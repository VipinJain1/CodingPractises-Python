# -*- coding: utf-8 

"""
Created on Wed Jul 21 13:58:18 2021

@author: VIP
https://www.geeksforgeeks.org/find-the-first-repeated-character-in-a-string/

Find the first repeated character in a string
Difficulty Level : Easy
Last Updated : 22 Apr, 2021
Given a string, find the first repeated character in it. We need to find the character that occurs more than once and whose index of second occurrence is smallest. A variation of this question is discussed here.
"""

def getFirstRepeatedChar(strdata):
    s = dict()
    for i in strdata:
        if i in s.keys ():
            print ("First Repeated Char is ", i)
            break
        else:
            s[i] =1
        
   
   
# First repeated chat program start Here.
import random as rd
import string
lower_upper_alphabet = string.ascii_letters
strdata = str()
for i in range (0,10):
    random_letter = rd.choice(lower_upper_alphabet)
    strdata = strdata + random_letter

print ("Sample string is" ,strdata )

getFirstRepeatedChar(strdata)




