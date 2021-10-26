# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 07:16:07 2021

@author: VIP
"""

class Solution:
 def myAtoi(self, s: str) -> int:
 s = s.strip()

 ln = len(s)

 if ln ==0:
 return 0
 if s[0].isalpha():
 return 0

 if ln ==1 and s in ('+','-'):
 return 0

 if s[0] in ('+', '-') and s[1] in ('+', '-'):
 return 0

 minus = False
 if 'e' in s.lower():
 index = (s.lower()).find('e')
 s = s[:index]


 ln = len (s)
 if ln ==0:
 return False
 if s.isalpha():
 return False
 if s[0] =='-':
 minus = True
 s = s[1:]
 if s[0] =='+':
 s = s[1:]


 news = str()
 for i in s:
 if i.isdigit():
 news = news +i
 else:
 break

 s = news 
 if s.isdigit() != True:
 return 0
 i = int (s)
 if minus == True:
 i = -i
 if i < -2147483648:
 i = -2147483648

 if i > 2147483647:
 i = 2147483647

 return i
