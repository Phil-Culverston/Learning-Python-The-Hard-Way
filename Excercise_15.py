# Imports argv so we can choose the file to open.
from sys import argv

# Setting the argv parameters as script and filename. Then opens the file.
script,filename = argv
txt = open(filename)

# Prints the filename to the user then reads out the content of the file.
print(f"Here's your file {filename}:")
print(txt.read())
# * Always use close after opening file as to disgard unneeded resources.
txt.close()

# Asks the user if they wish to look at another file.
print("Type the filename again:")
file_again = input(">")

# opens the file requested by user.
txt.again = open(file_again)

# Reads out the file.
print(txt_again.read())
txt.again.close()

# * - All comments marked with an asterisk are important for code optimisation.
# Messy comments on this one but full of important litte details :D
