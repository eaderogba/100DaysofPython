""" ***HIGHER OR LOWER GAME*** """
from art import logo, vs
from game_data import data
import random

# Print the logo from art
print(logo)

# Obtain the first piece to compare - find a way to randomly generate values from the dictionary, hint: the dictionary is a list
random_A = random.randint(0, len(data))
print(f"Compare A: {data[random_A]['name']} is a {data[random_A]['description']} from {data[random_A]['country']}")

# Storing follower count for A
follower_count_A = data[random_A]['follower_count']
# Test
print(follower_count_A)
# Output the 'VS' art
print(vs)

# Obtain the second piece to compare - find a way to randomly generate values from the dictionary, hint: the dictionary is a list
random_B = random.randint(0, len(data))
print(f"Against B: {data[random_B]['name']} is a {data[random_B]['description']} from {data[random_B]['country']}")

# Storing follower count for B
follower_count_B = data[random_B]['follower_count']
# Test
print(follower_count_B)

# Ask for user input
user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()
tries = 0
# Define a function here: Compare the value of followers that the key from Compare A had with that of Compare B. By accepting user input of either 'A' or 'B'.If follower count of sososos is greater than sosososo, and user answer is sooooo, print....
def compare_followers(answer, count_A, count_B, tries):
    if answer == 'A':
        if count_A > count_B:
            tries += 1
            print(f"You're right! Your score is {tries}")


        else:
            print(f"Sorry, that's wrong. Final score is {tries}")

    elif answer == 'B':
        if count_B > count_A:
            tries += 1
            print(f"You're right! Your score is {tries}")
        else:
            print(f"Sorry, that's wrong. Final score is {tries}")

compare_followers(user_answer, follower_count_A, follower_count_B, tries)
#elif .... print....Final Score would be the number of tries that the user has attempted thus far 

# The probelem now is i need to find a way to store tha correct answer, in case user is right, and use that to compare for the next user input. How do I do this???
# I also need to count the number of correct answers a user gets