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
guess = int(input("How many guesses do you want?"))
won = False
randomNum = generateRandom(min, max)

while guess > 0:
    counter += 1
    num = int(input(f"Guess the number (between {min} and {max}):"))
    if num < min or num > max:
        print("Number out of range")
    elif num == randomNum:
        won = True
        print(f"Congratulations. You guessed the number in {counter} attempts")
        break
    elif num > randomNum:
        print("Too high. Try again")
    else:
        print("Too Low. Try again")
    guess -= 1

if won == False:
    print(f"Sorry. You ran out of guesses. The correct Number is {randomNum}")

