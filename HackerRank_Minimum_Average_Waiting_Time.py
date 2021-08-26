# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 21:54:24 2021

@author: VIP
"""

def minimumAverage(customers):
    import heapq
    
    if len(customers) == 0:
        return  0
    if len(customers) == 1:
        return  abs ((customers[0])[1] - (customers[0])[0])
        
    dist = []
    sm =  []
    sum1 = 0
    cnt  = 0
    heapq.heapify(dist)
    for i in customers:
       heapq.heappush(dist, abs(i[1] -i[0]))
       cnt += 1

    for i in range (0,cnt):
        sum1 = sum(sm) + heapq.heappop(dist)
        sm.append(sum1)
        
    return int (sum(sm)/cnt)
    

customers = [[0, 3], [1, 9], [2, 6]]

print (minimumAverage(customers))

