# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 11:33:12 2021
https://leetcode.com/problems/print-zero-even-odd/

@author: VIP
"""

from threading import Lock

class ZeroEvenOdd(object):
    def __init__(self, n):
        self.n = n
        self.zero_lock = Lock()
        self.even_lock = Lock()
        self.odd_lock =  Lock()
        self.odd_lock.acquire()
        self.even_lock.acquire()
        
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        #determine if odd()/even() goes next
        for i in range(1, self.n+1):
            self.zero_lock.acquire()
            printNumber(0)
            if (i % 2 == 1):
                self.odd_lock.release()
            else:
                self.even_lock.release()
            
        
        
    def even(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(2, self.n+1, 2):
            self.even_lock.acquire()
            printNumber(i)
            self.zero_lock.release()
        
        
        
    def odd(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1, self.n+1, 2):
            self.odd_lock.acquire()
            printNumber(i)
            self.zero_lock.release()