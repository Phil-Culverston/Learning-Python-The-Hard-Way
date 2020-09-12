# Rewinds a file and gives them a number for each line within the file up to three lines.
# Importing argv 
from sys import argv 

# grabbing script and input_file from argv
script, input_file = argv

# Define print_all. 
def print_all(f):
	print(f.read())

# defines rewind and seeks line 0 the first line in the sample.txt file. 
# This sets a starting point for later. Whence can be used to default to 0.
def rewind(f):
	f.seek(0)

# gets line count everytime print_a_line is called. 
def print_a_line(line_count, f):
	print(line_count, f.readline())

# setting current_file to contain the strings pulled from the input_file (in this case sample.txt)
current_file = open(input_file)   

# Prints out a string then makes a newline.
print("First let's print the whole file:\n")

# Prints out everything contained within current_file (currently the contents of sample.txt)
print_all(current_file)

# Prints a string.
print("Now let's rewind, kind of like a tape.")

# Uses rewind on the current_file 
rewind(current_file)

# prints out a string.
print("Let's print three lines:")

# The next 3 lines are incremental and adds 1 to every line in the current_file variable. e.g.
# 1 First string in current_file
# 2 Second string in current_file
# 3 Third string in current_file
# <Nothing for a 4 as it only does this three times then stops. Can be fixed by making increments reoccur.>

current_line= 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

