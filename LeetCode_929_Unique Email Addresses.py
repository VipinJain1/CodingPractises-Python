# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 11:10:52 2021

@author: VIP
"""

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ln = len(emails)
        if ln ==0:
            return 0
        res  =[]
        #print (emails)
        for email in emails:
            if '@' in email:
                part1= email[0:email.index('@')]
                part2 = email[email.index('@')+1:]
                print ("Part1", part1)
                #print (part2)
                if ('.') in part1:
                    part1= part1.replace ('.','')
                if '+' in part1:
                    while ('+' in part1):
                        idx = part1.index('+')
                        part1 = part1[0:idx] 
                #print ("Part1", part1)    
                res.append(part1+ '@' + part2)    
            else:
                continue
        
        print (res)
        return len(set(res))