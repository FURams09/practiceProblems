collatz_dict = {}

def Collatz(maxStart, progress=1000):
    longestChain = [[0,0]]
    storedChain = []
    avgPath = 0
    for i in range(maxStart):
        currentCollatzLength = findCollatz(i + 1)
        storedChain.append([currentCollatzLength, i+1]) #keep a list of all of the             
##        if cnt > longestChain[0][0]: #the longestChain list is [cnt, startNumber]
##            longestChain = [[cnt, i]]
##        elif cnt == longestChain [0][0]:
##            longestChain.append([cnt, i])
        if (i + 1) % progress ==0:
            print i + 1
    storedChain = sorted(storedChain, key=lambda iterations: iterations[0], reverse=True)
    for j in range(len(storedChain)):
        avgPath += storedChain[j][0]
    avgPath = avgPath/float(len(storedChain))
    print 'mean average path length: ' + str(avgPath)
    print 'median average path length: ' + str(storedChain[maxStart/2])
    print 'largest combination: ' + str(storedChain[0])

def findCollatz(startNum):
    cnt = 0 #number of iterations, initialize to 0
    currNum = startNum
    while currNum > 1:
        if currNum % 2 == 0:
            currNum = currNum/2
            #print [i, collNum]
        else:
            currNum = currNum *3 +1
            #print [i, collNum]
            
        cnt += 1
    return cnt

def showAllCollatz(maxStart, viewPosition=0, viewRange =False):
    assert (type(viewPosition) is int), "viewPosition must be type int"
    assert (type(viewRange) is bool), "viewRange must be True or False"
    assert (type(maxStart) is int), "maxStart must be type int"
    allCollatz = []
    for i in range(1, maxStart+1):
        allCollatz.append([findCollatz(i), i])
        
    if viewPosition ==0:
        print sorted(allCollatz, key=lambda iterations: iterations[0], reverse=True)
    elif viewRange == False:
        print sorted(allCollatz, key=lambda iterations: iterations[0], reverse=True)[(viewPosition)]
    elif viewRange == True:
        print sorted(allCollatz, key=lambda iterations: iterations[0], reverse=True)[:(viewPosition)]
