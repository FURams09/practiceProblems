def spiralNumbers():
    #starting with one we will need to figure out the sum of all the diaginals
    #the four corners will be seperated by the the last spiral + 2. So for the first
    #spiral from one the corners are 3,5,7,9 (starting block) + 2 + 2 +2 +2, the next spiral is 13, 17, 21, 25 (starting block [9, the last corner] + 4 + 4 + 4 + 4
    #the length of the spiral with each corners grows by 2 so it'll be 1001-1/2 moves to calculate them all.

    runningTotal = 1 #starting point
    currentCorner = 1 #start at 0
    additiveValue = 2 #each corner starts 2 away but then
    while (additiveValue + 1) <= 1001: #the length of the outside row is the additive Value + 1, when this is 1001 we have our last row
        for i in range(4): #loop four times per square
            currentCorner = additiveValue + currentCorner
            runningTotal += (currentCorner)
        additiveValue += 2
    
    print runningTotal
