
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

	return factors
end

