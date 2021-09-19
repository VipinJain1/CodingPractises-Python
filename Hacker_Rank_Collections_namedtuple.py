# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 08:03:59 2021

@author: VIP
"""

import itertools 

L = [("a", 1), ("a", 2), ("b", 3), ("b", 4)]

key_func = lambda x:x[0]

for key, group in itertools.groupby (L, key_func):
    print (key + ":",  list (group))