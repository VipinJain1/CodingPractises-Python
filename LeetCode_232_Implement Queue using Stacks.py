# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 08:44:48 2021

@author: VIP
"""

class MyQueue:

 def __init__(self):
 self.stack = []


 def push(self, x: int) -> None:
 self.stack.append(x)


 def pop(self) -> int:
 v = self.stack[0]
 del self.stack[0]
 return v

 def peek(self) -> int:
 ln = len(self.stack)
 return self.stack[0]


 def empty(self) -> bool:
 ln = len(self.stack)
 if ln ==0:
 return True
 else:
 return False



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

