# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 17:57:25 2021

@author: VIP
"""

import random

random.seed(10000)
res = []
for i in range (0,9999):
    res.append(random.randrange(1,9999,1))
print (res)
