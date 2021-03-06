import random

#generate computer's number
Computer_number = random.randint(0, 20)
print("Your opponent has secretly selected number between 0-20\nYour goal is to guess the number!")
print("")
#Set loop to let user repeat the choice until they win
Outcome = 0

while Outcome < 6:
    #Let user to choose a number
    
    User_choice = input("Guess the number: ")
    print("")
    #Check if enetered value is int
    try:
        User_number = int(User_choice)
    except ValueError:
        print("Please do not enter floating numbers or strings! Try again...")
        print("")
        break

    User_choice = int(User_choice)
    if Computer_number > User_choice:
        print("Wrong! Your number is too low, please try again")
        print("")
        Outcome = 2
    elif Computer_number < User_choice:
        print("Wrong! Your number is too high, please try again")
        print("")
        Outcome = 4
    else:
        print("You win!!! Congratz!")
        print("")
        Outcome = 6

