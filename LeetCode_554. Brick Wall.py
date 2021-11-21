# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 17:54:34 2021

@author: VIP
"""


### NOT WORKING

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        data  = []
        ipdata  = []
        totalWall = len(wall)
        print ("Total wall",totalWall)
        for row in wall:
            sm =0
            res = []
            for val in  row:
                sm = sm +val
                res.append(sm)
            ipdata.append(res)    
        
        maxWall = 0
        print ("Exteped Wall",ipdata)  
        d= {}
        for idx, row in enumerate (ipdata):
            ln = len(row)
            if ln ==1:
                maxWall +=1
                
            print ("Row", row)
            for val in range (1, ln-1):
                if row[val] in d.keys():
                    d[row[val]].append(idx)
                else:
                    d[row[val]] =  [idx]
        mxval = 0
     
        for key, val in d.items():
            if len(val) > mxval:
                #print ("val",val)
                mxval = len(val)
        print ("Full Size Wall", maxWall)
        print ("mxval", mxval)
        if mxval ==0:
            return maxWall
        else:
            #mxval = maxWall +mxval 
            return totalWall - mxval
            
            
            
            
#Test Data 
wall = [[1,1],[2],[1,1]]
