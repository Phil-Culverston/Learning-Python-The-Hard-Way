# Defines the variable types_of_people with an integer value of 10
types_of_people = 10
# Defines x as a string. It also calls the previous variable.
x = f"There are {types_of_people} types of people."

# Defines the variable binary as a string.
binary = "binary"
# Defines the variable do_not as a string.
do_not = "don't"
# Defines the variable binary as a string and calls the two previous variables within the string.
y = f"Those who know {binary} and those who {do_not}."

# Prints out the value of x and y on two seperate lines.
print(x)
print(y)

# Prints out 2 strings on two seperate lines. Variables are also called, line 18 calls x and line 19 calls y.
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Defines the variable hilarious as False (boolean).
hilarious = False
# Defines joke_evaluation as a string.
joke_evaluation = "Isn't that joke so funny?! {}" # {} is an empty expression.

# Prints out the values of the two previously defined variables on lines 22 and 24.
#If the expression is not defined it is considered part of the string and simply text. e.g python will print out "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious)) # prints out the variable joke_evaluation and assigns hilarious to the previously empty expression

# Defining variables with strings again.
w = "This is the left side of..."
e = "a string with a right side."

# This merges the two previously defined variables on lines 31 and 32. So that both strings are merged into a single string which is then printed to the user. 
print(w + e)
