$amicableHash = Hash.new 0


def functionName
	getAmicableDict
	notSums = []
	for i in 1..28123
		if !isSumOfAmicable?(i)
			notSums.push(i)
		end
		puts i
	end

	puts notSums.inject(:+)
end


def isSumOfAmicable?(number)

	for i in 1..(number/2) #only need half the numbers since the other hafl are just a reversal of the first half. 

		if isAmicable?(i) and isAmicable?(number - i) 
			return true
		end
	end
	return false
end

def getAmicableDict
	#Create a list of all the amicable numbers
	for i in 1..28123 
		$amicableHash[i] = isAmicable?(i)	
	end

end

def isAmicable?(number)
	return number < getSumOfDivisors(number)
end


def getSumOfDivisors(numerator)
	factors = getPrimeFactors(numerator)
	exponent = 1 #Minimum number of occurances. Though it should always be set to a number
	factorSum = 0
	finalSum = 1 #start with one since it's multiplyiers. 

	while factors != []
		for i in 0..(factors.count(factors[0]))
			factorSum = factorSum + factors[0]**i
		end
		finalSum = finalSum * factorSum
		factorSum = 0
		factors.delete(factors[0])  #Remove the last
	end
	finalSum = finalSum - numerator
	return finalSum
end


def getPrimeFactors(numerator)
	d = 2
	i = 1
	factors = []
	factors_dict = Hash.new 0 #makes the default value for a hash 0 so that we can count the instances without checking if the value already exists
	while d*d <= numerator
		while numerator % d == 0
			factors.push(d)
			numerator = numerator /d
		end
		d = d + 1
	end
	if numerator > 1 
		factors.push(numerator)
	end

	factors.each do |factor|
		factors_dict[factor] += 1
	end
	return factors
end

=begin

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
=end
