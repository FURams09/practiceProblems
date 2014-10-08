from math import *
i = 0 #Number being tested for Primacy, started at 2
j = 1 #Potential divisor.
n = 0 #how many primes have been found
logSum = 0 
noOfPrimes = input('How many Primes would you like to calulate the sum of the logs?') #account for 2, could have done a check to see if a number was odd or even before incrementing but this will be quicker
isPrime = True


while n < noOfPrimes:
    
	i = i+2 #only need to check the odd numbers. Evens are always not prime.
	j = i - 1 #start by checking if the first number lower than this number is divisible. Will increment down one each time
	while j > 1:
		if i%j == 0:
			isPrime = False
			break #will force the next iteration to stop the loop
		j = j-1
	if isPrime ==True:
		logSum += log(i)
		n = n + 1
		#print i
		#print log(i)
		#print logSum
		
	isPrime = True
	if i % 2 == 0:
			i = i + 1 # make sure to only test the odd numbers after 2
print logSum			
print logSum / i
