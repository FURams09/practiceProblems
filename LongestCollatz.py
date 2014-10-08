collatz_dict = {}
#in general the lists/dictionary are [start number, number of iterations]
def Collatz(maxStart, progress=1000):
    global collatz_dict
    longestChain = [[0,0]]
    avgPath = 0
    for i in range(1, maxStart + 1):
        addCollatz(i)            
        if (i) % progress ==0:
            print i
    print (max(collatz_dict, key=collatz_dict.get))
##    collatz_dict = sorted(self.collatz_dict, key=lambda iterations: iterations[1], reverse=True)
##    for j in range(len(collatz_dict)):
##        avgPath += collatz_dict[j]
##    avgPath = avgPath/float(len(collatz_dict))
##    print 'mean average path length: ' + str(avgPath)
##    print 'median average path length: ' + str(storedChain[maxStart/2])
##    print 'largest combination: ' + str(storedChain[0])

def addCollatz(startNum):
    global collatz_dict
    #adds a number to a data dictionary
    cnt = 0 #number of iterations, initialize to 0
    currNum = startNum
    while currNum > 1:
        if currNum % 2 == 0:
            currNum = currNum/2
            #print [i, collNum]
        else:
            currNum = currNum *3 +1
            #print [i, collNum]

        if currNum in collatz_dict:
            cnt += collatz_dict[currNum] + 1 #the One is for the last number that led to the known.
            collatz_dict[startNum] = cnt
            return cnt
        cnt += 1
    collatz_dict[currNum] = cnt
    return cnt

def showAllCollatz(maxStart, viewPosition=0, viewRange =False):
    #used to display the full dictionary or find a specific entry. Can also show the first x entires
    assert (type(viewPosition) is int), "viewPosition must be type int"
    assert (type(viewRange) is bool), "viewRange must be True or False"
    assert (type(maxStart) is int), "maxStart must be type int"
    
    global collatz_dict = {}
    for i in range(1, maxStart+1):
        addCollatz(i)   
    if viewPosition ==0:
        print sorted( ((y,x) for y, x in collatz_dict.iteritems()), reverse=True)
    elif viewRange == False:
        print sorted( ((x,y) for y, x in collatz_dict.iteritems()), reverse=True)[(viewPosition)]
    elif viewRange == True:
        print sorted( ((x,y) for y, x in collatz_dict.iteritems()), reverse=True)[:(viewPosition)]
