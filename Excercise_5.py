name = 'Phil Culverston'
age = 35 # not a lie... apparently
height = 74 # inches
weight = 180 # lbs
kg = weight / 2.205 # Converts the weight from pounds to kilograms.
cm = height * 2.54 # converts the height from inches to centimeters.
eyes = 'Brown'
teeth = 'white'
hair = 'Black'


print(f"Let's talk about {name}.")  # A variable is called by using curly brackets {} within a defined string.
print(f"He's {height} inches or {cm} centimeters tall.") # Added in the conversion for lines 13 and 14. This was for an additional study drill.
print (f"He's {weight} pounds heavy. or {kg} kilograms.") # Added in the conversion for lines 13 and 14. This was for an additional study drill.
print(f"Actually that's not too heavy.") # The preceeding f on this line is redundant. It is used to enable variable calling within a string. The code will work with or without.
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# This line is tricky to get exactly right.
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")


# When defining a variable DO NOT USE an integer e.g. you can't define 1 = "phil" it must have a letter in front so a1 = "phil" would work
# 1 = phil - when uncommented will cause SyntaxError: cannot assign to literal
a1 = "phil" # However will work perfectly fine.

# In the excercise the converted height and weight will print out a long decimal number. round() can be used to combat this.
round_height = round(187.96)
round_weight = round(81.63265306122449)
print("==================== Rounding Example =========================")
print(f"{name}'s height when rounded up is {round_height} centimeters.")
print(f"{name}'s weight when rounded up is {round_weight} kilograms.")
