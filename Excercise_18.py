# This one is like argv in my previous scripts
def print_two(*args):
	arg1, arg2 = args
	print(f"arg1: {arg1}, arg2: {arg2}")

# Okay, that *args is actually pointless, we can just do.
def print_two_again(arg1, arg2):
	print(f"arg1: {arg1}, arg2: {arg2}")

# This just takes one argument
def print_one(arg1):
	print(f"arg1: {arg1}")

# This one takes no arguments
def print_none():
	print("I got nothin'.")

print_two("Phil","Culverston")
print_two_again("Phil", "Culverston")
print_one("First!")
print_none()