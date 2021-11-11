# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 17:57:25 2021

@author: VIP
"""

import random

random.seed(10000)
res = []
for i in range (0,10000):
    res.append(random.randrange(1,10000,1))
print (res)
