# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

p_letters = []
p_numbers = []
p_symbols = []

# Generate random letters
for _ in range(1, nr_letters + 1):
    p_letters.append(random.choice(letters))

# Generate random letters
for _ in range(1, nr_symbols + 1):
    p_symbols.append(random.choice(symbols))

# Generate random letters
for _ in range(1, nr_numbers + 1):
    p_numbers.append(random.choice(numbers))

# Concatenate the list and randomize
password_list = p_letters + p_numbers + p_symbols
random.shuffle(password_list)
concatenated_password = "".join(password_list)
print(f"Your PassWord is: {concatenated_password}")
