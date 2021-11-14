# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 10:51:17 2021

@author: VIP
"""

class MyStack:

    def __init__(self):
        self.stack = []
      
    def push(self, x: int) -> None:
        self.stack.append(x)
    def pop(self) -> int:
        return self.stack.pop()
        
    def top(self) -> int:
        v= self.stack[len(self.stack)-1]
        print (v)
        return v 

    def empty(self) -> bool:
        if len(self.stack) !=0:
            return False
        else:
            return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()