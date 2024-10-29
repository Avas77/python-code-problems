# generate a pair of random numbers between 1 and 6 
# display results
# ask if they want to roll the dice again

import random

def generateRandom():
    num1 = random.randint(1, 6)
    return num1

while True:
    ans = input("Roll the dice(y/n):").lower()
    if ans == "y":
        num1 = generateRandom()
        num2 = generateRandom()
        num_tuple = (num1, num2)
        print(num_tuple)
    else:
        print("Thank you for playing.")
        break

