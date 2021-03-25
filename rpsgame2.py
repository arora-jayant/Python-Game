import random

alloptions = ["rock", "paper", "scissors"]

print ("Welcome to my Rock-Paper-Scissors Game!")

usermove = input ("Please enter your move (Rock, Paper, or Scissors): ")

compoption = alloptions[random.randint(0, len(alloptions)-1)]

print ("The computer selected", compoption + ", and you selected", usermove + ".")

if usermove.lower() == "rock" and compoption.lower() == "rock":
    print ("It was a tie!")

elif usermove.lower() == "paper" and compoption.lower() == "paper":
    print ("It was a tie!")

elif usermove.lower() == "scissors" and compoption.lower() == "scissors":
    print ("It was a tie!")

elif compoption.lower() == "rock" and usermove.lower() == "scissors":
    print ("Rock crushes Scissors! Computer Wins!")

elif compoption.lower() == "scissors" and usermove.lower() == "paper":
    print ("Scissors cuts Paper! Computer Wins!")

elif compoption.lower() == "paper" and usermove.lower() == "rock":
    print("Paper covers Rock! Computer Wins!")

elif usermove.lower() == "rock" and compoption.lower() == "scissors":
    print ("Rock crushes Scissors! You Win!")

elif usermove.lower() == "scissors" and compoption.lower() == "paper":
    print ("Scissors cuts Paper! You Win!")

elif usermove.lower() == "paper" and compoption.lower() == "rock":
    print("Paper covers Rock! You Win!")

else:
    print ("There must have been a problem...Did you spell your move correctly?")

playagain = input ("Would you like to play again? Type 'no' to quit. ")

if playagain.lower() == 'no':
    print("Thanks for playing!")

else:
    print("Click 'run' to play again!")



