"""
Total numbers with no repeated digits in a range
Difficulty Level : Medium
Last Updated : 30 Dec, 2019
Given a range L, R find total such numbers in the given range such that they have no repeated digits.
For example:
12 has no repeated digit.
22 has repeated digit.
102, 194 and 213 have no repeated digit.
212, 171 and 4004 have repeated digits.

Examples:

Input : 10 12
Output : 2
Explanation : In the given range 
10 and 12 have no repeated digit 
where as 11 has repeated digit.

Input : 1 100
"""

def noRepeateDigits(s,d):
    d=[]
    
    for i in range(s,e+1,1):
        if i <10:
            d.append((i))
        elif str(i) ==  ''.join(set(str(i))):
            d.append (i)
    return d
            


s=9
e=89

print (noRepeateDigits (s,e))