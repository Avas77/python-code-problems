# random select number between 1 and 100
# ask user to guess number
# give hints if number is too low or high

import random

def generateRandom(min = 1, max = 100):
    num1 = random.randint(min, max)
    return num1

counter = 0
min = int(input("What is minimum range?:"))
max = int(input("What is maximum range?:"))
randomNum = generateRandom(min, max)

while True:
    counter += 1
    num = int(input(f"Guess the number (between {min} and {max}):"))
    if num < min or num > max:
        print("Number out of range")
    elif num == randomNum:
        print(f"Congratulations. You guessed the number in {counter} attempts")
        break
    elif num > randomNum:
        print("Too high. Try again")
    else:
        print("Too Low. Try again")

