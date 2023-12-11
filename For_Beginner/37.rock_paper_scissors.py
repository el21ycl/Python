# 
import random

while True:
    choices = ['rock', 'paper','scissors']

    computer = random.choice(choices)

    player = None
    while player not in choices:
        player = input('rock, paper, or scissors?: ').lower()
        if player in choices:
            continue
        else:
            print("Your input error!")
    print("computer: ",computer)
    print("player: ", player)
    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You Win!")
        if computer == "scissors":
            print("You Lose!")
    elif player == "paper":
        if computer == "rock":
            print("You Win!")
        if computer == "scissors":
            print("You Lose!")
    elif player == "scissors":
        if computer == "paper":
            print("You Win!")
        if computer == "rock":
            print("You Lose!")

    play_again = input("Play again? (Yes/No)").lower()

    if play_again != "yes":
        break
print("Bye")

