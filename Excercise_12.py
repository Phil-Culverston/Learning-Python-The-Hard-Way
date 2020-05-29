# Defining 3 variables and asking for the user input along with a print message.
age = input("How old are you?")
height = input("How tall are you?")
weight = input("How much do you weigh?")
luckynum = ("What is your lucky number?",input()) # Testing a funky prompt.

# Prints out the line.
print(f"""
So, you're {age} old, {height} tall and {weight} heavy. and your
lucky number is {luckynum}
""") # luckynum will fail to prompt the user. As stated this is a funky prompt.
