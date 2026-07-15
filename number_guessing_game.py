print("===== Number Guessing Game =====")

import random

secret_number = random.randint(1, 10)

guess =int(input("guess a number between 1 and 10: "))

while guess != secret_number:
    print("Wrong guess. try again!")

    if guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

    guess = int(input("guess again:"))
print("congratulations! you guessed the correct number!")
