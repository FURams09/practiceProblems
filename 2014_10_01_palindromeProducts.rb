class DailyProblem
	
	def self.threeDigitPalindrome
	i1 = 100
	i2 = 100
	currMax = 0
	lastMax = 0
	
		while i2 <= 999
			while i1 <= 999
				currMax = (i1 * i2).to_s
                puts i1.to_s + ' ' + i2.to_s
				if self.isPalindromeAlt?(currMax)
					if currMax.to_i > lastMax
						lastMax = currMax.to_i
						firstNum = i1
						secNum = i2
					end
				end
				i1 += 1
			end
            i1 = 100
			i2+= 1
            puts i2
		end
		puts 'The Largest Palindrome that is the product of two three digit number is ' + lastMax.to_s
		puts 'The two numbers that ' + lastMax.to_s + ' is a prodcut of are ' + firstNum.to_s + ' and ' + secNum.to_s
	end
	
	def self.isPalindrome?(productOf)
        
		if productOf.length == 1
            return true
		elsif productOf[0] != productOf[-1]
			return false
		elsif productOf.length == 2
			return true
		else
			(isPalindrome?( productOf[1.. -2]))
        end
 
	end
	
	def self.isPalindromeAlt?(productOf)
		productOf == productOf.reverse
	end

end
