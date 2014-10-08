from string import *

def countSubStringMatch(target, key):
    cnt = 0
    keyLoc = find(target, key) #first location
    while keyLoc > -1:
        cnt += 1 
        keyLoc = find(target, key, keyLoc + 1)
    print(cnt)
                   



def countSubStringMatchRecursive(target, key):
    
    if find(target, key) == -1:
        return 0
    else:
        return 1 + countSubStringMatchRecursive(target[find(target, key) + 1:], key)            
        
