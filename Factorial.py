def fact(n):

    if  n ==0:
        return True

    return ( n * fact(n-1))

n = int (input (" Enter Nmmber:" ))
print ( "n === ", n)
print (fact(n))