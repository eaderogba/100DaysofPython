"""***THE HANGMAN GAME****"""
import random
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages

# Program randomly chooses a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
word_length = len(chosen_word)