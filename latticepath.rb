def latticeCount(sizeA)
	latGrid = []
	#add first row, every point from [0,1] to [0,20] has exactly one way to get there. Add one to account for the 0th position
	latGrid << Array.new(sizeA + 1, 1)

	for i in 1..sizeA
		#add the first position which is always 1
		latGrid << Array.new([1])
		#i is going to be the grid above the current grid since we start with that first row of all ones
		for j in 1..sizeA 
			#the number of steps to get to any one point is the number of steps to get to the spot above it latGrid[i-1] + the number of paths to get to the square to it's left 
			latGrid[i] << latGrid[i][j-1] + latGrid[i-1][j]
		end
		puts latGrid[i]
		puts '--------'

	end
	puts latGrid[sizeA][sizeA]
	
end