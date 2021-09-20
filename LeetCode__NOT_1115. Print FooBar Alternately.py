# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 09:52:35 2021
1115. Print FooBar Alternately

@author: VIP
"""

from threading import Lock

class FooBar:
    def __init__(self, n):
        self.n = n
        self.lock1 = Lock()
        self.lock2 = Lock()
        self.lock2.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            self.lock1.acquire()
            printFoo()
            self.lock2.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            self.lock2.acquire()
            printBar()
            self.lock1.release()