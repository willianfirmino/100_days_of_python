import random

names_string = input("Give me everybody's names, separated by a comma. ")

names = names_string.split(", ")

who_is_paying = random.randint(0, len(names) - 1)

print(f"{names[who_is_paying]} is going to buy the meal today!")