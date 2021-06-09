from random import *
user=input("ROCK, PAPER, SCISSOR?   Shoot  \n")
comp=randint(0,2)
if comp == 0:
    comp = "rock"
elif comp == 1:
    comp = "paper"
else :
    comp = "scissors"

if comp == user:
    print("It is a tie!"+user+"/"+comp)
elif user == "rock" and comp == "scissors":
    print("You win")
elif user == "scissors" and comp == "paper":
    print("You win")
elif user == "paper" and comp =="rock":
    print("You win")
else :
    print("You lose")