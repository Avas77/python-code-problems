# prompt user to choose either rock, paper or scissors
# computer randomly selects its choice
# display both choices 
# determine winner
import random

choice_emo = {
    "r": "🪨",
    "p": "🧻",
    "s": "✂️"
}

play_again = True

while play_again:
    while True:
        random_choice = random.choice(list(choice_emo.keys()))
        choice = input("Rock, paper or scissors (r/p/s):")
        if choice in choice_emo.keys():
            print(f"Computer chose: {choice_emo[random_choice]}")
            if (choice == random_choice) or (choice == "r" and random_choice == "p") or (choice == "p" and random_choice == "r") or (choice == "s" and random_choice == "p"):
                print("Stalemate")
            elif (choice == "r" and random_choice == "s") or (choice == "p" and random_choice == "r") or (choice == "s" and random_choice == "p"):
                print("You won")
            else:
                print("Computer won")
            break
        else:
            continue

    user_ans = input("Do you want to play again? (y/n)")
    while True:
        if user_ans.lower() == "y":
            play_again == True
            break
        elif user_ans == "n":
            play_again = False
            break
        else:
            continue
    