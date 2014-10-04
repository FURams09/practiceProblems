def Collatz():
    collNum = 1 #the most recent number in the chain, initialize to 1
    longestChain = [[0,0]]
    storedChain = []
    for i in range(collNum, 10000):
        cnt = 0 #number of iterations, initialize to 0 
        while collNum > 1:
            knownCount = getIterations(storedChain, collNum)
            if i == 74:
                assert 'i == 74'
            if knownCount != 0:
                cnt += knownCount
                break
            if collNum % 2 == 0:
                collNum = collNum/2
                #print [i, collNum]
            else:
                collNum = collNum*3 +1
                #print [i, collNum]
            cnt += 1
##        if cnt > longestChain[0][0]: #the longestChain list is [cnt, startNumber]
##            longestChain = [[cnt, i]]
##        elif cnt == longestChain [0][0]:
##            longestChain.append([cnt, i])
        storedChain.append([cnt, i])
        #print storedChain
        collNum = i + 1
        cnt = 0
    print sorted(storedChain, key=lambda iterations: iterations[-0], reverse=True)

def getIterations(knownIterations, findNum):
    #look up if the next number in the Collatz pattern has already been found. 
    for i in range(len(knownIterations)):
        if knownIterations[i][1] == findNum:
            return knownIterations[i][0]
    return 0
