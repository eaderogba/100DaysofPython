"""***THE HANGMAN GAME****"""
import random
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages

# Program randomly chooses a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Create blanks
display = ["_" for _ in chosen_word]

# Testing code
print(chosen_word)

# An empty list. Stores the word
print(logo)
print(f"Your chosen word has this number of characters: {' '.join(display)}")

# Initialize the number of lives
lives = 6
game_over = False
while not game_over:
    # Program asks user to guess a letter, and outputs the length of the word
    guess = input("Guess a letter: ").lower()
    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    if guess in chosen_word:
        # Blanks are replaced with the guess
        for i in range(word_length):
            if guess == chosen_word[i]:
                display[i] = guess
        print(f"{' '.join(display)}")
    else:
        # Reduce the lives in decrement of 1
        lives -= 1
        print(f"Sorry, the {guess} you entered is not in the chosen word.")
        print(stages[lives])
     # Check if the user has won or lost
    if "_" not in display:
        print("You win")
        game_over = True
    elif lives == 0:
        print("Sorry, you have used all lives. You lose")
        game_over = True