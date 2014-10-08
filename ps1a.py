i = 1 #Number being tested for Primacy
j = 1 #Potential divisor. 
noOfPrimes = 1 #account for 2, could have done a check to see if a number was odd or even before incrementing but this will be quicker
isPrime = True

while noOfPrimes < 1000:
	i = i+2 #only need to check the odd numbers. Evens are always not prime. 
	j = i - 1 #start by checking if the first number lower than this number is divisible. Will increment down one each time
	while j > 1:
		if i%j == 0:
			isPrime = False
			j = 2 #will force the next iteration to stop the loop
		j = j-1
	if isPrime ==True:
		noOfPrimes = noOfPrimes + 1
		print 'Prime No ' + str(noOfPrimes)  + ' is ' + str(i)
	isPrime = True
