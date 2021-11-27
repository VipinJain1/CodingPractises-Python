# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 11:10:42 2021

5923. Minimum Number of Buckets Required to Collect Rainwater from Houses

@author: VIP
"""

class Solution:
    def minimumBuckets(self, street: str) -> int:
        
        
        ln = len(street)
        if ln ==0:
            return -1
        res =0
        st = set(street)
        
        if ln ==1:
            if street[0] =='.' or st.pop() == '.':
                return 0
            if street[0] =='H':
                return -1
        if  st.pop() == '.':
            return 0
        
        cnt =0
        first =False
        second = False
        for i in street:
            if i =='H':
                if first ==False:
                    first = True
                    continue
                if first ==True and second ==False:
                    second = True
                    if cnt >=1:
                        res = res +cnt
                    cnt =0
                    first = True
                    second = False
                    continue
            if first ==True:
                cnt +=1
        if res ==0:
            return -1
        else:
            return res
        
street=".HH.HH.HH.HH..H"

obj = Solution()
ret = obj.minimumBuckets(street)
print ("OP==", ret)
