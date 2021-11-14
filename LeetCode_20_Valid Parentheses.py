# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 10:51:48 2021

@author: VIP
"""

class Solution(object):
    def isValid(self, s):
        while "()" in s or "{}" in s or '[]' in s:
            s = s.replace("()", "").replace('{}', "").replace('[]', "")
        return s == ''