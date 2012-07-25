people = 30
cars = 40
buses = 15

if cars > people:
	print "Whe should take the cars"
elif cars < people:
	print "We should not take the cars"
else:
	print "We can`t decide"

if buses > cars and cars < people:
	print "That`s too many buses"
elif buses < cars or people > buses:
	print "Maybe we could take the buses"
else:
	print "We still can`t decide"

if people > buses:
	print "All right, let`s just take the buses"
else:
	print "Fine, let`s stay home then"


