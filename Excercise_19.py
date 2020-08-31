# Creates a function that contains a script and some variables. In this case a few lines about the amount of cheese and crackers we have.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print(f"You have {cheese_count} cheeses!")
	print(f"You have {boxes_of_crackers} boxes of crackers!")
	print("Man that's enough for a party!")
	print("Get a blanket.\n")
# Adds sets 20 cheese and 30 crackers. 
print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)

# Uses variables we have set in our own script not the ones inside the function, with new vales 10 and 50.
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# Same sort of thing as above but this time we are also adding two variables inside a single variable.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Simple division in order to get the sum inside the corresponding variable.
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# Taking everything above and combining it into one example. 
# Proving you can take the functions variables and play around with them however you like.
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)