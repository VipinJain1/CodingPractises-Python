class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        ln = len(s)
        ln1 = len(t)

        if ln1 < ln:
            return False
        cnt =0
        found =False
        s1  =[]
        t1 = []
        
        if ln ==0:
            return True
        
        s1[:] = s
        t1[:] = t
        for i in s1:
            if i in t1:
                cnt = t1.index(i)
                found  = True
                t1 = t1[cnt+1:]
                
            else:
                found = False
                return found
                
        if found == True:
            return True
        
                
                        