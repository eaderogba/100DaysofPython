import random

# Ask user for the names of people
names = input("How many people are having the meal? ").split(", ")

# List to store names of persons, after looping through each name
list_names = []
for _ in names:
    list_names.extend(names)

# Outputs Person to pay the bill
print(random.choice(list_names))