from sys import argv

script, filename = argv

print "Here is your file %s: " %(filename)
open_file = open(filename)
print open_file.read()
print "Now closing it"
print open_file.close()



