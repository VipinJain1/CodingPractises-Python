# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 13:27:02 2021

@author: VIP
"""

import heapq
# K Closetst Number


def kClosestNumber(a, k, x):
    ln = len(a)
    result = []
    if ln < k:
        return a
    d = dict()

    for i in a:
        num = abs(i - x)
        if num in d.keys():
            d[num].append(i)
        else:
            d[num] = [i]
    res = heapq.nsmallest(k, d.items(), key=lambda x: x[0])
    result = list(map(lambda x: x[1], res))
    import itertools
    return list(itertools.chain(*result))[0:k]


a = [1, 5, 3, 4, 6, 73, 4, 6, 78, 98, 3, 576]
k = 7
x = 7
print(kClosestNumber(a, k, x))
