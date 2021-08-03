# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 18:08:07 2021

https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

@author: VIP
"""

h =[1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5 ,5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]

h = [1,3,1,3,1,4,1, 3, 2, 5 ,5 ,5 ,5, 5, 5, 5 ,5, 5, 5 ,5 ,5 ,5 ,5 ,5, 5, 5 ]

word  = 'zaba'
word = 'abc'


def getCharNum(ch):
    return (ord (ch.upper()) - 65)

def designerPdfViewer(h, word):
    # Write your code here
    
    max =0
    for i in word:
        w = h[getCharNum(i)]
        if max < w:
            max = w
            
    return  (max *len(word))
        
    
print (designerPdfViewer(h, word))