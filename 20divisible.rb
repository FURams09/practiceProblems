class FindDivisible
	@@thruNum = 15
	@@primeDivisors = (1..@@thruNum).to_a
	def self.findNum
		currNum = @@thruNum
		foundAnswer = false

		while foundAnswer == false do

			if divCheck currNum, (@@primeDivisors.length) -1  #recursively check currNum modulo every number under 20
				puts 'the smallest number divisible by all numbers 1-'+ @@thruNum' is ' + currNum.to_s
				return
				#don't really need to set foundAnswer to true since return will just end the code but this will be
				#a good reminder of  why it was there. 
				#foundAnswer == true
			else
				currNum += 1
			end


		end 
	end

	def self.divCheck (topNumber, bottomNumber)
		puts topNumber.to_s + ' ' + bottomNumber.to_s + ' ' + @@primeDivisors[bottomNumber].to_s
		if bottomNumber == 0
			true
		elsif (topNumber % @@primeDivisors[bottomNumber] == 0) 
		 	divCheck(topNumber, (bottomNumber -1))
		 else
		 	false
		end
	end

	
end