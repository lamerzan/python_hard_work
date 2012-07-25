from random import randint


print "generating random number"
number = "%d%d%d" % (randint(1, 5), randint(1, 5), randint(1, 5))
print number