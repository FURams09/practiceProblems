def getAmicable(throughNum=10000, progressIndicator=1000):
    amicable_dict = {}
    amicableNumbers = []
    for i in range(1, throughNum + 1): #add one 
        amicable_dict[i] = sumOfDivisorsPrime(i)    
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


def sumOfDivisorsPrime(startNumber):
    n = startNumber
    factors = []
    factor_dict = {} #key = prme number value = factor
    d=2
    currSum = 0
    currProd = 1
    while d*d <= n: #only need to go up through the sqrt of the number for some reason
        while (n%d) == 0:
            factors.append(d)
            n /= d
        d += 1
    if n > 1:
        factors.append(n)
    # print sums these are the prime factors
    #Creates dictionary. See initialization for explaination. 
    for i in range(len(factors)):
        if factor_dict.has_key(factors[i]) is False:
            factor_dict[factors[i]] = factors.count(factors[i])

    #loops through dictionary calculating the sum of the primes (sum(keys**0..value) * sum(keys+1**0..value+1).. sum(keys+len(keys)**value+len(keys))
    for k, v in factor_dict.items():
        for l in range(v+1): #finds the upper exponential bound
            currSum += k**l
        currProd *= currSum
        currSum = 0
    return currProd - startNumber
        
        
