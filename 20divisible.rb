def findNum
	currNum = 20
	foundAnswer = false

	while foundAnswer == false do
		if divCheck currNum, 20 #recursively check currNum modulo every number under 20
			puts 'the smallest number divisible by all numbers 1-20 is ' + currNum.to_s
			return
			#don't really need to set foundAnswer to true since return will just end the code but this will be
			#a good reminder of  why it was there. 
			#foundAnswer == true
		else
			currNum += 1
		end


	end 
end

def divCheck (topNumber, bottomNumber)
	puts topNumber
	if bottomNumber == 1
		true
	elsif (topNumber % bottomNumber == 0) 
	 	divCheck(topNumber, (bottomNumber -1))
	 else
	 	false
	end
end