# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 16:56:38 2021

@author: VIP
"""

class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.data = {1: big, 2: medium, 3: small}
        
   
    def addCar(self, carType: int) -> bool:
        if self.data[carType]:
            self.data[carType] -= 1
            return True
        else:
            return False
        
# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)