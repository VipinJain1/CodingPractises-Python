# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 18:31:58 2021

@author: VIP
"""

def countGoodTriplets(arr, a, b, c):
    cnt = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                if (abs(arr[i] - arr[j]) <= a) and (abs(arr[j]-arr[k]) <= b) and (abs(arr[i]-arr[k]) <= c):
                    cnt = cnt + 1
    return(cnt)


arr = [3,0,1,1,9,7]
a =7
b =2
c =3                

print (countGoodTriplets(arr,a,b,c))