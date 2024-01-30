#Password Generator Project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(',')', '*', '+']

password = ""

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
choice_randomize = input("Would you like the letters, numbers and symbols in your password to be orderly put together or not? (y or n)\n")

if choice_randomize == "y":
    for letter in range(nr_letters):
        letter = random.choice(letters)
        password += f"{letter}"
    for number in range(nr_numbers):
        number = random.choice(numbers)
        password += f"{number}"
    for symbol in range(nr_symbols):
        symbol = random.choice(symbols)
        password += f"{symbol}"
    print(f"Your new and secure password: {password}")
elif choice_randomize == "n":
    for letter in range(nr_letters):
        letter = random.choice(letters)
        password += f"{letter}"
    for number in range(nr_numbers):
        number = random.choice(numbers)
        password += f"{number}"
    for symbol in range(nr_symbols):
        symbol = random.choice(symbols)
        password += f"{symbol}"
    pass_list = list(password)
    random.shuffle(pass_list)
    randomized_pass = "".join(pass_list)
    print(f"Your new and MORE secure password: {randomized_pass}")
else:
    print("I am verry sorry but you typed incorrectly. You must have typed 'y' or 'n'.")
