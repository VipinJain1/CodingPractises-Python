# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 15:30:21 2021

@author: VIP
"""

class TwoSum:

    def __init__(self):
        self.data = {}
     
    def add(self, number: int) -> None:
        if number in self.data.keys():
            self.data[number] +=1
        else:
            self.data[number] =1  
      
    def find(self, value: int) -> bool:
        for i in self.data.keys():
            if (value - i in self.data.keys()) and (value != 2*i):
                return True
            elif (value -i in self.data.keys()) and (value -i == i) and (self.data[i] >=2):
                return True
            else:
                return False
                
        

# Your TwoSum object will be instantiated and called as such:
obj = TwoSum()
for number in range (0,12):
    obj.add(number)
value =6
param_2 = obj.find(value)
print (param_2)