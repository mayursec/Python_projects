import random
play = "yes"

while play == "yes":
    choice = ["rock","paper","scissor"]

    com = random.choice(choice)
    

    hum =input("Your choice(rock/paper/scissor):")

    print("you chose",hum)
    print("com choose",com)
    if hum == "paper" and com == "rock":
        print("You won")
    elif hum=="paper" and com == "paper":
        print("Draw")
    elif hum == "paper" and com == "scissor":
        print("You lost")
    elif hum=="rock" and com=="rock":
        print("Draw")
    elif hum ==  "rock" and com=="paper":
        print("You lost")
    elif hum == "rock" and com=="scissor":
        print("you won")
    elif hum == "scissor" and com == "rock":
        print("You lost")
    elif hum =="scissor" and com == "paper":
        print("You won")
    elif hum == "scissor" and com == "scissor":
        print("Draw")
    else:
        print("Invalid option")
    play = input("Play again?")





        