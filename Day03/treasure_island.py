"""***Adventure game***"""

# Program asks user for direction
crossroad_choice = input(
    "You're at a crossroad. Where do you want to go? Type 'left' or 'right': \n").lower()
if crossroad_choice == "left":
    swim_wait = input(
        "You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. \n")
    if swim_wait == "wait":
        choose_door = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?").lower()
        if choose_door == "red":
            print("It's a room full of fire. Game Over.")
        elif choose_door == "blue":
            print("You entered a room of beasts. Game Over.")
        elif choose_door == "yellow":
            print("You Win!")
        else:
            print("Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You have fallen inside a hole. Game Over!")
