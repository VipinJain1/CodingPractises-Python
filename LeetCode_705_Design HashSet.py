# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 11:00:12 2021

@author: VIP
"""

class MyHashSet:

    def __init__(self):
        self.hashSet = set()
        

    def add(self, key: int) -> None:
         self.hashSet.add(key)

    def remove(self, key: int) -> None:
        if key in self.hashSet:
            self.hashSet.remove(key)
        

    def contains(self, key: int) -> bool:
        if key in self.hashSet:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)