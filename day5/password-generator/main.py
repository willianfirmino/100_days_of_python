# Password Generator Project
import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# my first solution

rand_password = ""

for i in range(nr_letters):
    rand_password = letters[random.randint(0, len(letters) - 1)]

for i in range(nr_numbers):
    rand_password += numbers[random.randint(0, len(numbers) - 1)]

for i in range(nr_symbols):
    rand_password += symbols[random.randint(0, len(symbols) - 1)]


rand_password = "".join(random.sample(rand_password, len(rand_password)))

print(rand_password)

# original solution.

rand_password = ""

for i in range(1, nr_letters + 1):
    rand_password += random.choice(letters)

for i in range(1, nr_numbers + 1):
    rand_password += random.choice(symbols)

for i in range(1, nr_symbols + 1):
    rand_password += random.choice(numbers)

print(rand_password)
