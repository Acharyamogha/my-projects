import random

def play():
    print("'r for rock, 'p' for paper, 's' for scissor:")
    user=input("Your choice: ")
    computer= random.choice(['r','p','s'])
    print("Computer choice is: ", computer)
    if user==computer:
        return 'It\'s a tie'
    
    if is_win(user, computer):
        return 'You Won!!'
    
    return 'You Lost'

def is_win(player,opponent):
       if (player=='r'and opponent=='s') or(player=='s'and opponent=='p') or (player=='p' and opponent=='r'):
           return True
       
       
print(play())