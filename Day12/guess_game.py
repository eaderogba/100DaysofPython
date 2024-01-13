"""*** GUESSING GAME ***"""

import random
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5

# Function to check user_guess against random_number
def check_guess(guess, random_number, lives):
    if guess > random_number:
        print("Too high")
        return lives - 1
    elif guess < random_number:
        print("Too low")
        return lives - 1
    else:
        print(f"You guessed the correct number {random_number}!")
    
# Function for user to chose difficulty
def difficulty():
    diff_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    while diff_level not in ('easy', 'hard'):
        diff_level = input(
            "Please choose a difficulty. Type 'easy' or 'hard': ").lower()
    if diff_level == "easy":
        return EASY_LEVEL
    elif diff_level == "hard":
        return HARD_LEVEL
    
# Guessing game Function
def guess_game():
    print(logo)
    print("You're Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

    # Computer generates a random number from 0 - 100
    random_number = random.randint(0, 100)

    print(f"Pssst, random number is {random_number}")
    # Set lives based on user input
    lives = difficulty()

    guess = 0
    while guess != random_number:
        print(f"You have {lives} attempts remaining to guess the number")
        # User guess a number
        guess = int(input("Make a guess: "))
        lives = check_guess(guess, random_number, lives)
        if lives == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != random_number:
            print("Guess again.")
guess_game()
