"""
Created on Thu Jul 22 07:33:24 2021

@author: VIP

https://www.geeksforgeeks.org/difference-two-given-times/

Difference between two given times
Difficulty Level : Medium
Last Updated : 22 May, 2020
Given two times in string “HH:MM” format. Here ‘H’ shows hours and ‘M’ shows minutes. You have to find the difference in the same string format between these two strings. But both given strings should follow these cases.
1) Time 1 will be less than or equal to time2
2) Hours will be possible from 0 to 23.
3) Minutes will be possible from 0 to 59

Examples:

Input : s1 = "14:00";
        s2 = "16:45";
Output : result = "2:45"

Input : s1 = "1:04"
        s2 = "13:05"
Output : result = "12:01"

"""


#ip  = { 0:2, 4:7, 21:23, 13:00, 12:00}

def minimum_time_difference(ip):
    mins= list()
    temp =0
    for key,value in ip.items():

        if key <12:

            temp = (key+24)*60 + value
            mins.append(temp)
        else:
            temp = (key)*60 + value
            mins.append(temp)

    m = 24*60*60
    for i in range (len (mins)):
        #print ("I==== ", i)
        for j in  range(i+1, len(mins) ):
            #print ("J === ",j)
            diff = abs(mins[i] - mins [j])
            #print ("diff  === ", diff)
            if (diff < m):
                m = diff
                #print (m)

    print ("Minimum time diference in minutes is " , abs(m))

# pass  input here.
ip= { 0:2, 4:7, 21:23, 13:00, 12:00}
minimum_time_difference(ip)