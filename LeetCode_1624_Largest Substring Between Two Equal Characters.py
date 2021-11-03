class Solution:
    def maxLengthBetweenEqualCharacters(self,s):
        ln = len(s)
        #print (ln)
        rev = s[::-1] #yxzbc
        mx=-1
       
        for i in range (0, ln):
            ch = s[i]
            ch1 = rev.index(ch)
            #print (ch1)
            if ch1 !=ln-i-1:
                size = ln -ch1 -i -2
                if size >mx:
                    mx = size
     
        if mx >=0:
            return mx
        else:
            return -1
                