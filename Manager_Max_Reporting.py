'''
Created on Wed Jul 21 13:58:18 2021

@author: VIP

https://www.geeksforgeeks.org/find-number-of-employees-under-every-manager/

Find number of Employees Under every Employee
Difficulty Level : Hard
Last Updated : 10 Jun, 2021
Given a dictionary that contains mapping of employee and his manager as a number of (employee, manager) pairs like below. 

{ "A", "C" },
{ "B", "C" },
{ "C", "F" },
{ "D", "E" },
{ "E", "F" },
{ "F", "F" } 

In this example C is manager of A, 
C is also manager of B, F is manager 
of C and so on.
 

Recommended: Please try your approach on {IDE} first, before moving on to the solution.
Write a function to get no of employees under each manager in the hierarchy not just their direct reports. It may be assumed that an employee directly reports to only one manager. In the above dictionary the root node/ceo is listed as reporting to himself. 
Output should be a Dictionary that contains following. 

A - 0  
B - 0
C - 2
D - 0
E - 1
F - 5 
Source: Microsoft Interview
This question might be solved differently but i followed this and found interesting, so sharing:
 
'''


def getCount(count,key, mgr):
    if key in mgr.keys():
        
        for i in mgr[key]:
            count = count+1
            count  = getCount (count, i, mgr)
    return  count
  
      
def getMgr(Hcy):
    
    count =0
    mgr = {}
    maxmgr = {}
    
    for key, val in Hcy.items():
        
        if val in mgr.keys():
            mgr[val].append (key)
        else:
            mgr[val] = [key]
        
        
     
    for key, val in mgr.items():
        count = getCount(count, key, mgr);
        maxmgr[key]  = count
        count  = 0

    print (maxmgr)
    
    mx =0
    cnr = str()
    for key,cnt in maxmgr.items():
        if  mx < cnt:
            
            mx = cnt
            cnr = key
     
    print ('Max reporting Mgr is' ,cnr , 'and total reports are', mx)
Hcy = {
       
       
       'A' : 'C',
       'B' : 'C',
       'D' : 'E',
       'E' : 'B',
       'F' : 'V',
       'A' : 'D'
       }


getMgr(Hcy)