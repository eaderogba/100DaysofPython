""" ***HIGHER OR LOWER GAME*** """
# Import the necessary functionalities
from art import logo, vs
from game_data import data
import random
import os
# Create a function to get a random account from data
def get_random_account():
    return random.choice(data)

# Store the account data into a printable format
def account_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

# A function to compare the number of followers
def compare_followers(answer, count_A, count_B):
    if answer == 'A':
        if count_A > count_B:
            return answer == "A"
    else:
        return answer == "B"

def game():
    tries = 0
    game_continue = True
    account_B = get_random_account()

    while game_continue:
        account_A = account_B
        account_B = get_random_account()
        while account_A == account_B:
            account_B = get_random_account()

        # Print the logo from art
        print(logo)
        # Print the comparison statements
        print(f"Compare: {account_data(account_A)}")
        # Output the 'VS' art
        print(vs)
        print(f"Against: {account_data(account_B)}")

        # Ask user for guess
        user_input = input("Who has more followers? Type 'A' or 'B': ").upper()
        # check if the user input is valid
        while user_input not in ['A', 'B']:
            user_input = input(
                "Who has more followers? Type 'A' or 'B': ").upper()

        # Compare the follower counts of the accounts
        is_correct = compare_followers(
            user_input, account_A["follower_count"], account_B["follower_count"])
        if is_correct:
            tries += 1
            print(f"You're right! Currecnt score: {tries}")
            os.system('clear')
        else:
            game_continue = False
            print(f"Sorry, that's wrong. Final Score: {tries}")
game()
