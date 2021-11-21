# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 08:14:25 2021

@author: VIP
"""

class LRUCache:
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.storage  = {}
        self.lru = []
        
    def get(self, key: int) -> int:
        if key in self.lru:
            self.lru.remove(key)
            self.lru.append(key)
        
        if key in self.storage.keys():
            ln = len(self.lru)
            return self.storage[key]
        return -1
    
    def put(self, key: int, value: int) -> None:
        #print ("Orig Capacity", self.capacity)
        if len(self.storage) <self.capacity:
            self.storage[key] =value
            if key in self.lru:
                self.lru.remove(key)
            self.lru.append(key)
        else:
            #print ("Data in Dict", self.storage)
            if key in self.storage.keys():
                self.storage[key] =value
                self.lru.remove(key)
                self.lru.append(key)
            else:
                oldkey = self.lru[0]
                #print ("Key to remove==", oldkey)
                del self.storage[oldkey]
                self.storage[key] =value
                del self.lru[0]
                self.lru.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)