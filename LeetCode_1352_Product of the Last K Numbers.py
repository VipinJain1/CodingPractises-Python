# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 09:34:40 2021

@author: VIP
"""

class ProductOfNumbers:

    def __init__(self):
        self.data =[]
        self.prod =[]

    def add(self, num: int) -> None:
        self.data.append(num)
        
        if len(self.prod) ==0 or self.prod[-1] ==0 :
            self.prod.append(num)
        else:
            prod = self.prod[-1] * num
            self.prod.append(prod)
    
    def getProduct(self, k: int) -> int:
        #print ("len data", len(self.data))
        #print ("len prod", len(self.prod))
        if k > len(self.data):
            return -1
        if 0 in self.prod[-k:]:
            return 0
        else:
            if k == len(self.prod):
                return self.prod[-1]
            
            if self.prod[-k-1] == 0:
                div = 1
            else:
                div = self.prod[-k-1]
            prod = self.prod[-1]//div
            return prod
    
# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)