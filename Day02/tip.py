# Program welsomes the user
print("Welcome to the tip calculator!")

# Ask user for total money spent
total_bill = float(input("What was the total bill? \n$ "))
# Ask user for the percentage of tip they'd like to give
tip_percent = float(
    input("How much tip would you like to give? 10, 12, or 15? 12 \n")) / 100 + 1
# Ask for the total number of persons contributing to the bill
persons = int(input("How many people to split the bill? \n"))
# Print the amount of tip to be added to the total bill
print(f"Each person should pay: ${(total_bill / persons) * tip_percent:.2f}")
