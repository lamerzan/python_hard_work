<<<<<<< HEAD
from sys import argv

script, filename = argv

print "Here is your file %s: " %(filename)
open_file = open(filename)
print open_file.read()
print "Now closing it"
print open_file.close()



=======
from sys import argv

script, filename = argv

print "Here is your file %s: " %(filename)
open_file = open(filename)
print open_file.read()
print "Now closing it"
print open_file.close()



>>>>>>> 25d4598f734bce6b4a01b91180fd539d6f155bbc
