# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 14:38:15 2021

@author: VIP
"""







def beautifulTriplets(d, arr):
    
    """
    count  =0
    for i in  range (0, len(arr) -2):
        for j in  range (i+1, len(arr)-1):
            for k in  range (j+1, len(arr)):
                
                if( (i <j and j <k ) and (arr[j] - arr[i] ==d) and (arr[k] - arr[j] ==d)):
                    count  = count +1
    return count
    """       
    
    count  =0
    for i in  range (0, len(arr)):
        index1 =i
        try:
            if (arr[i]+d) in arr:
                index2 = arr.index (arr[i]+d)
                if (arr[index2] +d)  in arr:
                    index3 = arr.index(arr[index2] +d)
                    if (index2 and index3):
                        count +=1
        except:
            return count
        #print ([index1,index2,index3])
    return count      




arr =[1,6,7,7,8,10,12,13,14,19]
d =3
print (beautifulTriplets(d,arr))