$numbers = {1 => "one", 2 => "two", 3 => "three", 4 => "four", 5 => "five", 6 => "six", 7 => "seven",  8 => "eight",  9 => "nine", 10 => "ten", 11 => "eleven", 12 => "twelve", 13 => "thirteen", 14 => "fourteen", 15 => "fifteen", 16 => "sixteen", 17 => "seventeen", 18 => "eighteen", 19 => "nineteen" }
$tens = {2 => "twenty", 3 => "thirty", 4 => "fourty", 5 => "fifty", 6 => "sixty", 7 => "seventy", 8 => "eighty", 9 => "ninety"}

def getNumLetters 
	total = 0 
	for i in 1..1000 
		total += getNumberSum(i)
		puts i
	end
	puts total
end



def getNumberSum (intValue) 
	if intValue == 0
		return 0
	end

	currentPlaceValue = 0
	if intValue / 1000 > 0 #there are thousands place
		currentPlaceValue = $numbers[intValue/1000].length + "thousand".length + getNumberSum(intValue%1000)
	elsif intValue / 100 >0
		currentPlaceValue = $numbers[intValue/100].length + "hundred".length
		if intValue % 100 != 0 #there are tens or ones so we need to add an and
			currentPlaceValue += "and".length
		end
		currentPlaceValue += getNumberSum(intValue%100)
	elsif intValue/10 > 0 && intValue>= 20 #anything less than 20 is just the number value
		currentPlaceValue = $tens[intValue/10].length + getNumberSum(intValue % 10)		
	else  #we are down to the ones place thsi is our return value
		currentPlaceValue =  $numbers[intValue].length
	end

	if currentPlaceValue > 0  
		return currentPlaceValue
	else
		return 0
	end
end