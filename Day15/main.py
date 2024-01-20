"""*** COFFEE MACHINE ***"""
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# To keep track of profit
total_money = 0 

# Gets the coffee details
def coffee_details(coffee_type):
    return MENU.get(coffee_type, None)

# Gets the cost of a specific coffee type
def get_coffee_cost(coffee_type):
    coffee_info = coffee_details(coffee_type)
    return coffee_info["cost"] if coffee_info else None

# To check available resources for a specific coffee type
def check_resources(coffee_type):
    coffee_info = coffee_details(coffee_type)
    if coffee_info:
        coffee_ingredients = coffee_info["ingredients"]
        return all(resources.get(ingredient, 0) >= amount for ingredient, amount in coffee_ingredients.items())
    return False

# To deduct available resources after a successful transaction
def deduct_resources(coffee_type):
    if check_resources(coffee_type):
        coffee_ingredients = coffee_details(coffee_type)["ingredients"]
        for ingredient, amount in coffee_ingredients.items():
            resources[ingredient] -= amount
        return True
    return False

# Main function to handle user prompts
def user_prompts():
    global total_money 
    program_end = False
    while not program_end:
        # TODO 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino)
        user_query = input("What would you like? (espresso/latte/cappuccino) ").lower()
        coffee_choice = ["espresso", "latte", "cappuccino"]
        maintenance_query = ["off", "report"]

        if user_query in coffee_choice:
            coffee_cost = get_coffee_cost(user_query)
            if coffee_cost is not None:
                print(f"Your cost is {coffee_cost}")
                # TODO 4: Check resources sufficient?
                if check_resources(user_query):
                    print("Please insert coins.\n")
                    quarters = int(input("How many quarters? "))
                    dimes = int(input("How many dimes? "))
                    nickels = int(input("How many nickels? "))
                    pennies = int(input("How many pennies? "))

                    # TODO 5: Process coins
                    total_dollars = ((quarters * 25) + (dimes * 10) + (nickels * 5) + pennies) / 100.0
                    change = total_dollars - coffee_cost
                    # TODO 6: Check transaction successful?
                    if coffee_cost > total_dollars:
                        print("Sorry that's not enough money. Money refunded.")
                    else:
                        # TODO 7: Make Coffee
                        print(f"Here is ${change:.2f} in change.\nHere is your {user_query} ☕️. Enjoy!")
                        deduct_resources(user_query)
                        total_money += coffee_cost
                else:
                    print("Sorry! Not enough Resources.")
            else:
                print("Invalid coffee type")

        elif user_query in maintenance_query:
            # TODO 3: Print report
            if user_query == "report":
                for key, value in resources.items():
                    print(f"{key}: {value}")
                print(f"Total money made so far: ${total_money:.2f}")
            # TODO 2: Turn off the Coffee Machine by entering “off” to the prompt
            elif user_query == "off":
                program_end = True
user_prompts()