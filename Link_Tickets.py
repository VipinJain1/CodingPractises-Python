# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 07:33:24 2021

@author: VIP

https://www.geeksforgeeks.org/find-itinerary-from-a-given-list-of-tickets/

Find Itinerary from a given list of tickets
Difficulty Level : Medium
Last Updated : 01 Jun, 2021
Given a list of tickets, find itinerary in order using the given list.
Example: 
 

Input:
"Chennai" -> "Banglore"
"Bombay" -> "Delhi"
"Goa"    -> "Chennai"
"Delhi"  -> "Goa"

Output: 
Bombay->Delhi, Delhi->Goa, Goa->Chennai, Chennai->Banglore,
It may be assumed that the input list of tickets is not cyclic and there is one ticket from every city except final destination.
One Solution is to build a graph and do Topological Sorting of the graph. Time complexity of this solution is O(n).
We can also use hashing to avoid building a graph. The idea is to first find the starting point. A starting point would never be on ‘to’ side of a ticket. Once we find the starting point, we can simply traverse the given map to print itinerary in order. Following are steps. 

"""

def  findStartLocation(tkts):
    
     for i in tkts.keys():
         
         if i not in  tkts.values():
             
             return i
         
def linkTickets(tkts):
    
    startlocation = findStartLocation(tkts)
    #print (startlocation)
    
    ln  =  len(tkts)
    
    while ( ln >0 ):
        print (startlocation,tkts[startlocation])
        ln = ln-1
        startlocation = tkts[startlocation]

tkts = {
    
    'Chennai' :'Bangalore',
    'Bombay' : 'Delhi',
    'Goa' : 'Chennai',
    'Delhi': 'Goa'
    }

linkTickets(tkts)



