# 13. Write a script to get the maximum and minimum value in a dictionary.
def keywithmaxval(d):
    """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
    v=list(d.values())
    k=list(d.keys())
    return k[v.index(max(v))]

def keywithminval(d):
    """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
    v=list(d.values())
    k=list(d.keys())
    return k[v.index(min(v))]
  
dic1 = {1:10, 2:20,3:30, 4:40,5:20,6:60,7:20}
dicMax = dic1[keywithmaxval(dic1)]
dicMin = dic1[keywithminval(dic1)]
print(dicMax)
print(dicMin)