from sys import argv # Imports argv so we can choose the file to open.

# Setting the argv parameters as script and filename. Then opens the file.
script,filename = argv
txt = open(filename)

# Prints the filename to the user then reads out the content of the file.
print(f"Here's your file {filename}:")
print(txt.read())

# Asks the user if they wish to look at another file.
print("Type the filename again:")
file_again = input(">")

# opens the file requested by user.
txt_again = open(file_again)

# Reads out the file.
print(txt_again.read())
