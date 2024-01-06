import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_choice = [rock, paper, scissors]

# The game function
def rock_paper_scissors():
    # Ask user for input
    user_input = int(input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
    if user_input in range(0, 3):
        print(f"You choose {user_input} \n {game_choice[user_input]}")
        # Computer choice generation
        computer_input = random.randint(0, 2)
        print(
            f"Computer choose {computer_input} \n {game_choice[computer_input]}")
    else:
        print("Type 0 for Rock, 1 for Paper or 2 for Scissors.")
    while user_input not in range(0, 3):
        rock_paper_scissors()

    # compare the user's and the computer's choice to determine the winner (or a draw)
    if user_input == 0 and computer_input == 2:
        print("You win")
    elif computer_input == 0 and user_input == 2:
        print("You lose")
    elif user_input > computer_input:
        print("You win")
    elif computer_input > user_input:
        print("You lose")
    else:
        print("Draw")

rock_paper_scissors()