""" ***CIPHER PROGRAM*** """

from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Function takes the 'text', 'shift_amount' and 'cipher_direction' as inputs.
# The 'caesar' function, shifts each letter of the 'text' forwards or backwards in the alphabet by the shift number and prints the encrypted text.


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            move = alphabet.index(char) + shift_amount
            end_text += alphabet[move % 26]
        else:
            end_text += char
    print(f"The encoded text is '{end_text}'")


cipher_over = False
while not cipher_over:
    print(logo)
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    # Keep prompting user if input for direction not met
    while direction not in ('encode', 'decode'):
        print("Invalid direction.")
        direction = input(
            "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    # Take other inputs from user once direction is satisfied
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number: "))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    # To restart program, depending on user's choice
    restart = input(
        "Type 'yes' if you want to go again. Otherwise 'no'.\n").lower()
    if restart == 'no':
        cipher_over = True
        print("Goodbye")
