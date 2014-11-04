

def getSquares(maxBound = 100)
	primeList = []
	for i in 2..maxBound
		for j in 2..maxBound
			if !primeList.include?(i**j)
				primeList.push(i**j)
			end
		end
	end

	puts primeList.length
end