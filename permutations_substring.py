S = "abbc"
A= "abcbcdfgabacbbac"
s = sorted (S)

for i in range (0,len(A),len(S)):

    s1 = sorted (A[i:i+len(S)])

    if (s1 == s):
        print (A[i:i+len(S)])




