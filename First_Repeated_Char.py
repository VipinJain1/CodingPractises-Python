S = "ABCA"

s = dict()
       
for i in S:
    
    if   i in s.keys ():
        print (i)
        break
    else:
        s[i] =1
        
    