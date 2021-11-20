# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 15:47:08 2021

@author: VIP
"""

class MapSum:

    def __init__(self):
        self.map ={}
        

    def insert(self, key: str, val: int) -> None:
        self.map[key]=val
        

    def sum(self, prefix: str) -> int:
        sm =0
        ln = len(prefix)
        for i in self.map.keys():
            if prefix == i[:ln]:
                sm = sm + self.map[i]
        return sm
                
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)