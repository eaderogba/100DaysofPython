import random

# Ask user for the names of people. names should be separated by a comma followed by a space.
names = input("How many people are having the meal? ").strip().split(", ")

# Outputs Person to pay the bill
print(random.choice(names))
