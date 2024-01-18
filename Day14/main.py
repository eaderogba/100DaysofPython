""" ***HIGHER OR LOWER GAME*** """
from art import logo, vs
from game_data import data
import random

# Print the logo from art
print(logo)

# Obtain the first piece to compare - find a way to randomly generate values from the dictionary, hint: the dictionary is a list
def random_generator_A():
    random_A = random.randint(0, len(data))
    print(f"Compare A: {data[random_A]['name']} is a {data[random_A]['description']} from {data[random_A]['country']}")
    # Storing follower count for A
    count_A = data[random_A]['follower_count']
    return count_A

# Obtain the second piece to compare - find a way to randomly generate values from the dictionary, hint: the dictionary is a list
def random_generator_B():
    random_B = random.randint(0, len(data))
    print(f"Against B: {data[random_B]['name']} is a {data[random_B]['description']} from {data[random_B]['country']}")
    # Storing follower count for B
    count_B = data[random_B]['follower_count']
    return count_B

# Ask for user input
tries = 0

# Define a function here: Compare the value of followers that the key from Compare A had with that of Compare B. By accepting user input of either 'A' or 'B'.If follower count of sososos is greater than sosososo, and user answer is sooooo, print....

game_over = False
while not game_over:
    FOLLOWER_COUNT_A = random_generator_A()
    # # Output the 'VS' art
    print(vs)
    FOLLOWER_COUNT_B = random_generator_B()

    user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    if user_answer == 'A':
        if FOLLOWER_COUNT_A > FOLLOWER_COUNT_B:
            tries += 1
            print(f"You're right! Your score is {tries}")

        else:
            print(f"Sorry, that's wrong. Final score is {tries}")
            game_over = True
    elif user_answer == 'B':
        if FOLLOWER_COUNT_B > FOLLOWER_COUNT_A:
            tries += 1
            print(f"You're right! Your score is {tries}")
        else:
            print(f"Sorry, that's wrong. Final score is {tries}")
            game_over = True
    elif FOLLOWER_COUNT_A == FOLLOWER_COUNT_B:
        print("They have equal number of followers")
        game_over = True

    #compare_followers(user_answer, FOLLOWER_COUNT_A, FOLLOWER_COUNT_B, tries)
# elif .... print....Final Score would be the number of tries that the user has attempted thus far

# The probelem now is i need to find a way to store tha correct answer, in case user is right, and use that to compare for the next user input. How do I do this???
# I also need to count the number of correct answers a user gets
