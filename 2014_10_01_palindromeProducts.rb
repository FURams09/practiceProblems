class DailyProblem
	
	def threeDigitPalindrome
	i1 = 100
	i2 = 100
	currMax = 0
	lastMax = 0
	
		while i2 <= 999
			while i1 <= 999
				currMax = (i1 * i2).to_s
                puts i1.to_s + ' ' + i2.to_s
				if isPalindrome?(currMax)
					if currMax.to_i > lastMax
						lastMax = currMax.to_i
					end
				end
				i1 += 1
			end
            i1 = 100
			i2+= 1
            puts i2
		end
		puts 'The Largest Palindrome that is the product of two three digit number is ' + lastMax.to_s
	end

	def isPalindrome?(productOf)
        if productOf.length == 1
            return true
        end
    	if (productOf[0] == productOf[-1]) && (isPalindrome?( productOf[1.. -2]))
			true
		else
			false
		end
	end

end
