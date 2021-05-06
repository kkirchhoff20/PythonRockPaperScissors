from random import randint


def gameloop():
    resume = True
    while(resume):
        computerPlay = getComputerPlay()
        userPlay = getUserPlay()
        if(computerPlay == userPlay):
            print("Draw.")
            continue
        win = processTurn(computerPlay, userPlay)
        if(win):
            print("Computer plays " + computerPlay + ". ")
            print("Congratulations! You win!")
        else:
            print("Computer plays " + computerPlay + ". Better luck next time.")
        print("Play again?")
        response = input()
        while(response not in acceptableInput2):
            print("Please respond either Yes or No")
            response = input()
        if(response == "No"):
            resume = False


def getComputerPlay():
    play = ""
    rand = randint(1, 4)
    if(rand==1):
        play = "Rock"
    elif(rand==2):
        play = "Paper"
    else:
        play = "Scissors"
    return play


def getUserPlay():
    play = ""
    print("Enter your play")
    play = input()
    while(play not in acceptableInput):
        print("Please enter your move as either Rock, Paper, or Scissors")
    return play


def processTurn(computerplay, userplay):
    win = False
    if(userplay == "Rock"):
        if(computerplay == "Scissors"):
            win = True
    elif(userplay == "Scissors"):
        if(computerplay == "Paper"):
            win = True
    else:
        if(computerplay == "Rock"):
            win = True
    return win


acceptableInput = ["Rock", "Scissors", "Paper"]
acceptableInput2 = ["Yes", "No"]
print("Let's play Rock Scissors Paper!")
input("Press any key to continue")
gameloop()
print("Thank you for playing!")