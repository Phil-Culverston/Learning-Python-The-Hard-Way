print("How old are you?",end='') # end ='' tells python not to end the line with a newline character go to the next line
age = input() # Awaits an input from the user. The input is then stored into the assigned variable
print("How tall are you?",end='')
height = input()
print("How much do you weigh?",end='')
weight = input()

# Once all three of the variables have been given values from the user through input().
# This line prints out the values back to the user.
print(f"So, you're {age} old, {height} tall and {weight} heavy.")
