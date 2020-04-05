print("Mary had a little lamb.")
print("It's fleece was white as {}{}".format('snow')) # snow is NOT a variable it is simply a string that is being used for the empty expression {} in the previous string.
print("And everywhere that Mary went.")
print("."* 10) # multiplies the string by 10. Essentially creates a line of dots ..........

# Defining 10 variables each with a single character within a string.
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# prints out the word CheeseBurger using each variable as a character in the Word. Removing the , on line 21 will cause SyntaxError: invalid syntax
# This is because python has not been told that it needs to define a new variable within the code.
print(end1 + end2 + end3 + end4 + end5 + end6, end='')
print(end7 + end8 + end9 + end10 + end11 + end12)
