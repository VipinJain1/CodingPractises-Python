A = 'abcd'
B ='cdabcdab'

def findSubstrMinCount(A,B):
    count =0

    while (True):
        if B in A:
            return count
        else:
            A = A+A
            count  +=1

        if count  == 1000:
            return False

print(findSubstrMinCount(A,B))
