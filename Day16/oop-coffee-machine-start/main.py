"""*** COFFEE MAKER ***"""
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Creates an instance of the MoneyMachine class to handle money-related operations
money_machine = MoneyMachine()

# Creates an instance of the CoffeeMaker class to manage the coffee-making process
coffee_maker = CoffeeMaker()

# Creates an instance of the Menu class to manage available the drinks
menu = Menu()

# Prints a report of available resources in the coffee maker
coffee_maker.report()

# Prints a report of the money status
money_machine.report()

is_on = True
while is_on:
    # Gets the available drink options from the menu
    options = menu.get_items()
    # Asks the user for their choice of drink
    choice = input(f"What would you like?({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        # Give user picks a coffee, program checks resources and payment, then makes and serves the coffee
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
