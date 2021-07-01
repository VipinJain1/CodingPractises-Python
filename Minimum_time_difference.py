
#ip  = { 0:2, 4:7, 21:23, 13:00, 12:00}

def minimum_time_difference(ip):
    mins= list()
    temp =0
    for key,value in ip.items():

        if key <12:

            temp = (key+24)*60 + value
            mins.append(temp)
        else:
            temp = (key)*60 + value
            mins.append(temp)

    m = 24*60*60
    for i in range (len (mins)):
        #print ("I==== ", i)
        for j in  range(i+1, len(mins) ):
            #print ("J === ",j)
            diff = abs(mins[i] - mins [j])
            #print ("diff  === ", diff)
            if (diff < m):
                m = diff
                #print (m)

    print ("Minimum time diference in minutes is " , abs(m))

# pass  input here.
ip= { 0:2, 4:7, 21:23, 13:00, 12:00}
minimum_time_difference(ip)