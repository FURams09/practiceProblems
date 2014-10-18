def getAmicable(throughNum=10000, progressIndicator=1000):
    amicable_dict = {}
    amicableNumbers = []
    for i in range(1, throughNum + 1): #add one 
        amicable_dict[i] = sumOfDivisors(i)    
    print 'Dictionary Complete'
    for k, v in amicable_dict.items():
        if k% progressIndicator == 0:
            print k
        if v <= throughNum and v > 0 and k != v: #don't check if the value is less than 1 (the lowest number we care about) or higher than throughNum (the highest number we care about) or if the key and value are the same
            if amicable_dict[v] == k:
                amicableNumbers.append(k) 
    return 'the answer is : ' + str(sum(amicableNumbers))
def sumOfDivisors(startNumber):
    sum = 0
    for i in range(1, startNumber):  #don't want to know that the start number divides itself
        if startNumber % i == 0:
            sum += i
    return sum
            
        
