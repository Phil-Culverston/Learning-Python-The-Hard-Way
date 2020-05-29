# Imports the argv library (go C++! :D)/module.
from sys import argv
# Assigns the variables to the left from argv.
# argv is the argument/flag used when executing the script. A bit like ls -a <-
script,first,second,third = argv

# Prints out the now assigned variables.
print("The script is called:",script)
print("Your first variable is:",first)
print("Your second variable is:",second)
print("Your third variable is:",third)
