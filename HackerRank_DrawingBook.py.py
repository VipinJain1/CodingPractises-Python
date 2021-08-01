# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 08:44:19 2021

https://www.hackerrank.com/challenges/drawing-book/problem

Drawing Book

A teacher asks the class to open their books to a page number. A student can either start turning pages from the front of the book or from the back of the book. They always turn pages one at a time. When they open the book, page  is always on the right side:

@author: VIP
"""


emails = []

n  = int (input())

for i in range (n):
    emails.append(input())
    
#emails  = ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']


def validateExtn(email):
    stillGood = True
    lst = email.split ('.')
    if len(lst) !=2:
        stillGood = False
    else:
        extn = lst[1]
        if len(extn) !=3:
            stillGood = False
        for i in extn:
            if i.isdigit():
                stillGood = False
                         
        
    return  stillGood

def validateName(email):
    stillGood = True
    lst = email.split ('@')
    if (len(lst) !=2):
        stillGood = False
    else:
        extn = lst[0]
       
        for i in extn:
            if  i.isdigit() or i.isalnum()  or i =='-' or i == '_' :
                stillGood = True
            else:
              stillGood = False  
    return stillGood

def validateDotAndAtRFate(email):
    stillGood = True
    cnt =0
    cnt1 =0
    for i in email:
        if i =='@':
            cnt = cnt +1
            if cnt >1:
                stillGood = False
                
        if i == '.':
            cnt1 = cnt1+1
            if cnt >1:
                stillGood = False
    return stillGood
        
  
        
        
def validateEmails(emails):
         
    
    for email in emails:
    
               
        if ( validateExtn(email)):
             if  validateName(email):
                 if validateDotAndAtRFate(email):
                     print (email)
                 else:
                     continue 
             else:
                 continue
        else:
            continue 




validateEmails(emails)


