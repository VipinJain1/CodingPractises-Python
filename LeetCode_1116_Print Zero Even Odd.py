# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 22:29:29 2021

@author: VIP
"""

class ZeroEvenOdd:
    def __init__(self, n):
        self.count = 0
        self.cnt   = 0
        self.zero  = 1
        self.even  = 1
        self.odd   = 1

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        if self.count == 0:
            print (0)
            self.count = 1
            self.cnt +=1
            self.zero = 0
            
        if self.even == 0 or self.odd  == 0:
            print (0)
            self.cnt +=1
            self.even = 1
            self.odd =  1
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        if self.cnt %2 == 0 and self.zero  == 0 :
            print (cnt)
            self.even  = 0
            self.cnt +=1
            if self.cnt == n:
                return
            self.cnt +=1
        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        if self.cnt %2 != 0 and self.zero  == 0 :
            print (cnt)
            self.odd = 0
            if self.cnt == n:
                return
            self.cnt +=1
        