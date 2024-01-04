############### Blackjack Project #####################

import random
from art import logo
import os
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
blackjack = 21
ace = 11


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


# A deal_card() function that uses the List below to *return* a random card. 11 is the Ace.
def deal_card():
    return random.choice(deck)
# Calculate_score() takes a List of cards as input and returns the score.


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
# Check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 represents a blackjack in our game.
    if sum(cards) == blackjack and len(cards) == 2:
        return 0

# Function also checks for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in cards and sum(cards) > blackjack:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
# Compares user and computer scores, providing messages for different scenarios.


def compare(user_score, computer_score):
    if user_score > blackjack and computer_score > blackjack:
        return "You went over. You lose"
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, your opponent has a blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > blackjack:
        return "You went over. You lose"
    elif computer_score > blackjack:
        return 'Your opponent went over. You win!'
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose"

# Deal the user and computer 2 cards each


def play_game():
    print(logo)
    user_cards = [deal_card() for _ in range(2)]
    computer_cards = [deal_card() for _ in range(2)]
    is_game_over = False
    # Score is rechecked with every new card drawn and the checks repeated until the game ends.
    while not is_game_over:
        # Calling calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(
            f"Computer's first card: {computer_cards[0]}")
        # If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
        if user_score == 0 or computer_score == 0 or user_score > blackjack:
            is_game_over = True
        else:
            user_should_deal = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Once the user is done, the computer should keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(
        f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


# Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear_console()
    play_game()
