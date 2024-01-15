"""*** Number Guessing Game ***"""

import random
from art import logo
EASY_LEVEL = 10
HARD_LEVEL = 5

# Function to set difficulty based on user choice
def difficulty():
    diff_level = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
    while diff_level not in ('easy', 'hard'):
        diff_level = input(
            "Please choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
    if diff_level == "easy":
        return EASY_LEVEL
    elif diff_level == "hard":
        return HARD_LEVEL

# Check if user input is same as the randomly generated number by the computer
def check_guess(guess, number, lives):
    if guess > number:
        print("Too high")
        return lives - 1
    elif guess < number:
        print("Too low")
        return lives - 1
    else:
        print("Yes! You guessed right.")

# Create function for the game
def game():
    print(logo)
    print("You're Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    # Generate a random number
    random_number = random.randint(0, 100)
    # Test
    print(f"Psst, {random_number}")
    lives = difficulty()
    game_over = False
    # Re-rerun the program after lives == 0, or user guess is equal to random number generated
    while not game_over:
        print(f"You have {lives} remaining.")
        user_guess = int(input("Enter a number guess from 0 - 100: "))
        lives = check_guess(user_guess, random_number, lives)
        if user_guess != random_number and lives != 0:
            print("guess again")
        elif lives == 0:
            print(f"You have {lives} remaining. Game Over")
            restart = input("Do you want to play again Enter 'yes' or 'no': ").strip().lower()
            if restart == "yes":
                game()
                # reset lives
                lives = difficulty()
            else:
                game_over = True
        else:
            restart = input("Do you want to play again Enter 'yes' or 'no': ").strip().lower()
            if restart == "yes":
                game()
                # reset lives
                lives = difficulty()
            else:
                game_over = True
game()

