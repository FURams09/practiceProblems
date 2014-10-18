

$months = {1 => 31, 2 => 28, 3 => 31, 4 => 30, 5 => 31, 6 => 30, 7 => 31, 8 => 31, 9 => 30, 10 => 31, 11=>30, 12 =>31}
$day = [:sunday, :monday, :tuesday, :wednseday, :thursday, :friday, :saturday]

	def getNumberOfFirsts(startYear, throughYear,dayToCount)
		#0 will be Sunday, 1 will be Monday etc.
		currentMonth = 1
		currentYear = 1900
		numberOfSundays = 0
		dateOfFirst = 1 # 01/01/1900 is a Monday, this is established. therefor 12/31/

		
		for i in currentYear..2000
			for j in currentMonth..12
				dateOfFirst = getFirstOfMonth(j, i, dateOfFirst) #will be the first day of next month
				puts 'month ' + (j).to_s + ' year ' + i.to_s + ' day of Next first ' + $day[dateOfFirst].to_s
				if dateOfFirst == 0 and i >= startYear #need to calculate dates from 1900 but don't want to start calculating the number of Sundays til 1901
					
					numberOfSundays += 1
				end
			end
			currentMonth = 1
		end
		puts numberOfSundays
	end

	def getFirstOfMonth(month, year, startDay) 

		if  (year%4 == 0 and year%100 != 0) or (year%100 ==0 and year%400==0) and month == 2
			#special handling where if it's a leap year not divisible by 100 we have make it 29
			datesToAdd = 29 + startDay

		else
			datesToAdd = $months[month] + startDay
		end	
		return datesToAdd % 7 

	end