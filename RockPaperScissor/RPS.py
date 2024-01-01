import random
def play():
    user = input("Enter your option(Rock/Paper/Scissor) \n").lower()
    computer = random.choice(['rock', 'paper', 'scissor'])

    if user == computer:
        return "It's tie"
    if is_win(user, computer):
        return "You won"
    return "you lost"

def is_win(player, opponent):
    if (player == 'paper' and opponent == 'rock') or (player == 'scissor' and opponent == 'paper') or (player == 'rock' and opponent == 'scissor'):
        return True
print(play())