# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 07:33:24 2021

@author: VIP
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



