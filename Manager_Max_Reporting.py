
def getCount(count,key, mgr):
    if key in mgr.keys():
        
        for i in mgr[key]:
            count = count+1
            count  = getCount (count, i, mgr)
    return  count
  
      
def getMgr(Hcy):
    
    count =0
    mgr = {}
    maxmgr = {}
    
    for key, val in Hcy.items():
        
        if val in mgr.keys():
            mgr[val].append (key)
        else:
            mgr[val] = [key]
        
        
     
    for key, val in mgr.items():
        count = getCount(count, key, mgr);
        maxmgr[key]  = count
        count  = 0

    print (maxmgr)
    
    mx =0
    cnr = str()
    for key,cnt in maxmgr.items():
        if  mx < cnt:
            
            mx = cnt
            cnr = key
     
    print ('Max reporting Mgr is' ,cnr , 'and total reports are', mx)
Hcy = {
       
       
       'A' : 'C',
       'B' : 'C',
       'D' : 'E',
       'E' : 'B',
       'F' : 'V',
       'A' : 'D'
       }


getMgr(Hcy)