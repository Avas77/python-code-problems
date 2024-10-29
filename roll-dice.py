# generate a pair of random numbers between 1 and 6 
# display results
# ask if they want to roll the dice again

import random

def generateRandom():
    num1 = random.randint(1, 6)
    return num1

times = int(input("How many times do you want to roll the dice?"))

while times > 0:
    ans = input("Roll the dice(y/n):").lower()
    if ans == "y":
        num1 = generateRandom()
        num2 = generateRandom()
        num_tuple = (num1, num2)
        print(num_tuple)
    elif ans == "n":
        print("Thank you for playing.")
        break
    else:
        print("Invalid Choice")
    times -= 1

