# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 08:47:53 2021

@author: VIP
"""

def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score +=1
    return score

w = ["programming" ,"is" , "awesome"]

print (score_words(w))