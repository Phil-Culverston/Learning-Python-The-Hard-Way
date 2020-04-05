# Defines the variable formatter and adds 4 empty expressions.
formatter = "{} {} {} {}"

# Prints and assigns values to the above expressions using .format
print(formatter.format(1,2,3,4)) # assigns the numbers 1 to 4 in order within the empty expressions defined in formatter and prints them.
print(formatter.format("one", "two", "three", "four")) # Same thing on this line as with line 5 however the numbers are strings rather than integers.
print(formatter.format(True, False, False, True)) # Using boolean values to give a value to the formatter variables expressions.
print(formatter.format(formatter, formatter, formatter, formatter)) # causes a loop whereby formatter is called by itself 4 times. Ending up with a strings of 16 {}.
print(formatter.format( # The books asks you to try your own formatter. So I have used a line from the game Portal where the turret will ask if someone is there when they detect you.
    "'Hello,",
    "is anybody",
    "there?'",
    "said the turret"
  ))

# note the .format() is known as a function.
# The formatter variable is an array.
