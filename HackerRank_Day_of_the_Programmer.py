# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 22:50:26 2021

@author: VIP
"""


def dayOfProgrammer(year):
    # Write your code here
 
    jan =31
    mar = 31
    apr = 30
    may = 31
    jun = 30
    jul = 31
    aug = 31
    
    if year %4 == 0 and year >= 1700 and year <=1917:
        feb = 29
    elif year >= 1919 and ( (year % 400 ==0) or (year %4 ==0 and year %100 !=0)):
        feb = 29
    elif year == 2018:
        return '26.09.1918'
    else:
        feb =28
        
        
    dayOfProgrammer = 256
    total8Months = jan+ feb+mar+apr+may+jun+jul+aug
    day =   dayOfProgrammer -   total8Months
    return str (day) +  '.' + '09' + '.' + str (year)


year = 2016

result = dayOfProgrammer(year)
print (result)

    
    
