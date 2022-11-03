import random
from unittest import result
def get_choices ():
    player_choice = input("Enter the player  choice (rock,paper,scissors):")
    option = ["rock","paper","scissors"]
    computer_choice = random.choice(option)
    choices = {"player":player_choice , "computer":computer_choice}
    return choices 

def check_win (player ,computer):
    print (f"you chose  {player} , computer chose  {computer}")
    if player==computer:
        return "its a tie!"
    elif player == "rock":
        if computer == "scissors":
         return  " you  win"  
    else :
        return  " you lose"
    

    if player == "scissors":
        if computer == "rock":
         return  " you  lose"  
    else :
        return  " you win"
    
    if player == "paper":
        if computer == "rock":
         return  " you  lose"  
    else :
        return  " you win"
    

choices = get_choices()
result = check_win ( choices["player"] , choices ["computer"] )
print ( result)
