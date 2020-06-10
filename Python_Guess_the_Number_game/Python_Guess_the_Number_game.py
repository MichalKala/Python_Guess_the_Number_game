import random

#generate computer's number
Computer_number = random.randint(0, 20)
print("Your opponent has secretly selected number between 0-20\nYour goal is to guess the number!")

#Set loop to let user repeat the choice until they win
Outcome = 0

while Outcome < 6:
    #Let user to choose a number
    User_choice = input("Guess the number: ")
    #Check if enetered value is int
    try:
        User_number = int(User_choice)
    except ValueError:
        print("You enter something else than integer number, please do not enter floating numbers or strings!")
        break

    User_choice = int(User_choice)
    if Computer_number > User_choice:
        print("Wrong! Your number is too low, please try again")
        Outcome = 2
    elif Computer_number < User_choice:
        print("Wrong! Your number is too high, please try again")
        Outcome = 4
    else:
        print("You win!!! Congratz!")
        Outcome = 6

