# I am defining each variable with an integer (cars, space_in_a_car, drivers, passengers) then creating additional variables used for calculations.
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# Prints out the variables along with strings in order to print out the total sum of each additional variable.
# The additional variables are the ones I had created above. Print allows the end user to see the results of those additioanal variables.

print("There are",cars,"cars available.")
print("There are only",drivers,"drivers available.")
print("There will be",cars_not_driven,"empty cars today.")
print("We can transport",carpool_capacity,"people today.")
print("We have",passengers,"to carpool today.")
print("We need to put about",average_passengers_per_car,"in each car.")
