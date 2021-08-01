# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 11:27:51 2021
https://www.hackerrank.com/challenges/time-conversion/problem

Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example


Return '12:01:00'.


Return '00:01:00'.

Function Description

@author: VIP
"""


def timeConversion(s):
    # Write your code here
    
    ## AM Logic
    if 'pm' not in  s.lower():
        if s[0:2] == 12:
            hr = '00'
            return (hr + s[2:len(s) -2])
        else:
            return (s[0:len(s) -2])
    ## PM Logic
    else:
        if (s[0:2] == '12'):
            hr = '12'
            return (hr + s[2:len(s) -2])
        
        else:
            hr = str( int(s[0:2] ) + 12)
            return (hr + s[2:len(s) -2])
