def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1
    
    for key in questions:
        print("-------------------------------")
        print(key)
        for i in options [question_num-1]:
            print(i)
        guess = input("Enter (A,B,C,D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_anwer(questions.get(key),guess)
        question_num += 1

    display_score(correct_guesses,guesses)

    
def check_anwer(anwer,guess):
    if anwer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

def display_score(correct_guesses , guesses):
    print("-------------------------------")
    print("RESULTS")
    print("-------------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i) , end="")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i , end="")
    print()

    sore = int((correct_guesses/len(questions))*100)
    print("Your sore is: "+str(sore)+ "%")


def play_again():
    response = input("Do you wannt to play again? (Yes or No): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

# a dictionary named question
questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: " : "B",
    "Python is tributed to which comedy group?: " : "C",
    "Is the Earth round?: " : "A"
}

# 2D list
options = [
    ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
    ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D.SNL"],
    ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]
]

new_game()

while play_again():
    new_game()

print("Byeeeee")