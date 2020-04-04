# Opening statement to the program
print("I will now count my chickens:")

# prints out the total Hens

print("Hens",(float(25+ 30 / 6)))

# prints out the total Roosters
print("Roosters",(float(100 - 25 * 3 % 4)))

# Prints out the total eggs

print("Now I will count the eggs:")

# Calculates and prints out the sum.

print(float(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6))

# Checks to see if

print("Is it true that 3 + 2 < 5 -7?")

# Prints out false as the < (less than) operator asks the interpreter if this is true or false.

print(float(3 + 2 < 5 - 7))

# This would fail because there is no comma , after the closing bracket. This will cause a syntax error if not fixed. Note this also does not contain the excercise float point.

# print("What is 3 + 2?"3 + 2)
print("What is 5 - 7?",(float(5 - 7)))

print("Oh, that's why it's False.")
print("How about some more.")

# The true or false statement is also present here. Only different operators have been used e.g. >= and <=.

print("Is it greater?",(float(5 > -2)))
print("Is it greater or equal?",(float( 5 >=-2)))
print("Is it less or equal?",(float( 5 <=-2)))

# The operator -- is denoting that the integer -7 is in fact a negative number. Whereas in the 2nd line it will attempt to add 5 an 7 because python is incapable of reason :P
print (float(5 -- -7))
print (float(5 - -7))

# The % is what is known as a "Modulus or Modulo". It is NOT a percentage but rather it finds the remainder in a division for example 2 % 5 = 2 because it's not possible to divide 2, 5 times and so python will return the only number it logically can. The first logical number our [2] % 5.
# In contrast however if you do 5 % 2 you will end up with 1 because 5 / 2 is 2 with 1 remainder. Therefore it is 1.
print (float(2 % 5))
print (float(5 % 2))
