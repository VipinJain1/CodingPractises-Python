# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 14:20:18 2021

@author: VIP
"""

class MaxStack:
    def __init__(self):
        self.stack = []
    
    def push(self, x: int) -> None:
        self.stack.append(x)
    
    def pop(self) -> int:
        if len(self.stack)>0:
            x = self.stack.pop()
            return x
        return -1

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return -1
    
    def peekMax(self) -> int:
        if len(self.stack) >0:
            return max(self.stack)
        return -1
    
    def popMax(self) -> int:
            mx = max(self.stack)
            ln = len(self.stack)
            if ln >0:
                for i in range (ln-1, -1, -1):
                    if self.stack[i] ==mx:
                        del self.stack[i]
                        break
                return mx
            else:
                return -1

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()