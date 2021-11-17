# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 16:57:53 2021

@author: VIP
"""

class Logger:

    def __init__(self):
        self.logger = {}
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        shouldPrint = False
        if message not in self.logger.keys():
            shouldPrint = True
            self.logger[message] = timestamp +10
        elif self.logger[message] > timestamp:
            shouldPrint = False
        else:
            self.logger[message] = timestamp +10  
            shouldPrint = True
        
        return shouldPrint
            
        
# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)