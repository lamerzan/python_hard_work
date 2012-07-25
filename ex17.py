from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" %(from_file, to_file)

#we could do this two on one line
input = open(from_file)
indata = input.read()

print "Input file is %d bytes long" %len(indata)
print "Does the output file exists? %r" %exists(to_file)
print "Ready, hit RETURN to continue, or CTRL-C to abort."
raw_input()

output = open(to_file, 'w')
output.write(indata)

print "All right it done."

output.close()
input.close()