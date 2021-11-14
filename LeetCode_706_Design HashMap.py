# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 10:41:26 2021

@author: VIP
"""

class MyHashMap:

    def __init__(self):
        self.val = [None] * (10**6 +1) 
    def put(self, key: int, value: int) -> None:
        self.val[key] = value
     
    def get(self, key: int) -> int:
        if self.val[key] != None:
            return self.val[key]
        else:
            return -1
    def remove(self, key: int) -> None:
        if self.val[key] != None:
            self.val[key] = None

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)