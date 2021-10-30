# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 10:54:29 2021

@author: VIP
"""

class Solution:
    def uniqueMorseRepresentations(self, words):
        morse =[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        def morseRep(word):
            sm = str()
            loc = int()
            for i in word:
                loc = ord(i) - ord('a')
                sm = sm + morse[loc]
            return sm   
        d = {}
        for i in words:
            morseR = morseRep(i)
            if morseR in d.keys():
                d[morseR] += [i]
            else:
                d[morseR] = [i] 
           
        return (len (d.keys()))
            

words = ["rwjje","aittjje","auyyn","lqtktn","lmjwn"]
obj  = Solution()
print (obj.uniqueMorseRepresentations(words))
