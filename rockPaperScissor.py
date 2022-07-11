import random

user_win = 0
com_win = 0

options = ['rock', 'paper', 'scissor']

while True:
    user_input = input('Type rock/Paper/Scissor or Q to quit: ').lower()

    if user_input == 'q':
        print("If u want to play please restart the game.")
        break

    if user_input not in options:
        print("Please type rock/Paper/Scissor")
        continue

    random_num = random.randint(0,2)
    # 1.rock, 2.paper, 3.scissor
    computer_pick = options[random_num]
    print("computer picked", computer_pick, '.')

    if user_input == "rock" and computer_pick == "scissor":
        print("You won!")
        user_win+=1
    elif user_input == "scissor" and computer_pick == "rock":
        print("You won!")
        user_win+=1
    elif user_input == "paper" and computer_pick == 'rock':
        print("You won!")
        user_win+=1
    elif (user_input == 'paper' and computer_pick == 'paper') or (user_input == 'rock' and computer_pick == 'rock') or (user_input == "scissor" and computer_pick == 'scissor'):
        print("Both choose same. It is a tie.")
        continue
    else:
        print("You lost!")
        com_win+=1

print("You won", user_win, 'times.')
print("Computer won", com_win, 'times.')
print("GoodBye")

