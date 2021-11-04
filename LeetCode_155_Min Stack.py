# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 12:26:41 2021

@author: VIP
"""

class MinStack:

    def __init__(self):
        self.stack =[]
        self.minStack = []
    
    def push(self, val: int) -> None:
        if len(self.minStack) ==0:
            self.minStack.append(val)
        elif val <= self.minStack[len(self.minStack)-1]:
            self.minStack.append(val)
        self.stack.append(val)
    
    def pop(self) -> None:
        
        if len(self.stack) >0:
            self.val = self.stack.pop()
        if len(self.minStack) !=0 and self.val == self.minStack[len(self.minStack)-1]:
            self.minStack.pop()
    
    def top(self) -> int:
        if len(self.stack) >0:
            return self.stack[len(self.stack) -1]
    
    def getMin(self) -> int:
        if len(self.minStack) !=0:
            print (self.minStack)
            return self.minStack[len(self.minStack)-1]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

obj = MinStack()
obj.push(2)
obj.push(0)
obj.push(3)
min = obj.getMin()
print (min)
obj.push(0)
val = obj.pop()
print (val)
top = obj.top()
print (top)
min = obj.getMin()
print (min)






