# Bad Solution, Not done yet

class MaxStack:

    def __init__(self):
        self.stack =[]
        self.tempStack = []
        self.maxStack= []
 
    def push(self, x: int) -> None:
        if len(self.maxStack) ==0:
            self.maxStack.append(x)
        elif self.maxStack[len(self.maxStack)-1] <= x:
            self.maxStack.append(x)
        self.stack.append(x)
        
    def pop(self) -> int:
        if len (self.stack) >= 1:
            top = self.stack.pop()
            if (len (self.maxStack) >=1)  and (top ==  self.maxStack[len(self.maxStack) -1]):
                self.maxStack.pop()
            return top
   
    def top(self) -> int:
        ln = len(self.stack)
        if ln >= 1:
            return self.stack[ln-1]
        
    def peekMax(self) -> int:
        if len(self.maxStack) >=1:
            return self.maxStack[len(self.maxStack) -1]

    def popMax(self) -> int:
        mx = max(self.stack)
        ln = 
        self.stack.remove(mx)
        if mx == self.maxStack[len(self.maxStack) -1]:
            self.maxStack.pop()
            if len(self.maxStack) ==0 and  len(self.stack) !=0:
                self.maxStack.append(max((self.maxStack)))
        
            
    
     

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()