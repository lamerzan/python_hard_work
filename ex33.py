def INumbers(number, increment):
	i = 0
	numbers = []
	

	for i in range(number):
		print "At the top i is %d" %i
		numbers.append(i)
		i = i + increment
		print "Numbers now: ", numbers
		print "at the buttom i is %d" %i

	print "The numbers: "

	for num in numbers:
		print num



NumbersOfI = int(raw_input("Numbers of i>>  "))
IncrementNumbers = int(raw_input("Number of increment>> "))

INumbers(NumbersOfI, IncrementNumbers)

