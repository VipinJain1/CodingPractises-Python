# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 08:01:05 2021

@author: VIP
"""


class Solution:
    def calculate(self, s: str) -> int:
        ln =len(s)
        s = list (s)
        if ln ==0:
            return -1
        res = []
        cnt =0
        while (cnt<ln):
            print (s[cnt])
            if s[cnt] == ' ':
                cnt +=1
                continue
            
            if s[cnt].isdigit():
                res.append(int(s[cnt]))
                
            elif s[cnt] =='*':
                val = int (int (res.pop()  * int (s[cnt+1])))
                res.append(val)
                cnt +=1
            elif s[cnt] =='/':
                val = int (int (res.pop()  / int (s[cnt+1])))
                res.append(val)
                cnt +=1
            elif s[cnt] == '+':
                res.append(int (s[cnt+1]))
                cnt +=1
                                   
            elif s[cnt] == '-':
                res.append(-int(s[cnt+1]))
                cnt +=1
                           
            cnt +=1     
        
        return sum(res)
        
s = '2+2+5*7'
s= "2-2/5/5"
s =" 3/2 "
s =" 3+5 / 2 "
obj = Solution()
print (obj.calculate(s))

                