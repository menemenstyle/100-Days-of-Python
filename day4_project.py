# Rock Paper Scissors Generator

import random

rock = '''
    _______
---'    ____)
        (_____)
        (_____)
        (____)
---.____(___)
'''

paper = '''
    _______
---'    ____)____
          _______)
          ________)
          _______)
---.___________)
'''

scissors = '''
    _______
---'    ____)____
          _______)
          ________)
         (____)
---._____(___)
'''

gesture = [rock, paper, scissors]

computer = random.randint(0, len(gesture) - 1)
player = int(input(f"Welcome to the wonderful, chaotic game of Rock Paper Scissors!\nHere are the choices:\nRock: {rock}\nPaper: {paper}\nScissors: {scissors}\nWhat do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player == 0 or 1 or 2:
    print(f"Player chooses: {gesture[player]}\nComputer chooses: {gesture[computer]}")
else:
    print(f"I'm sorry. But there seems to be a problem because you typed wrong. Type 0 for Rock, 1 for Paper or 2 for Scissors.")
    
if player == 0:
    if computer == 0:
        print("It's a draw!")
    elif computer == 1:
        print("Computer wins!")
    elif computer == 2:
        print("Player wins!")
if player == 1:
    if computer == 0:
        print("Player wins!")
    elif computer == 1:
        print("It's a draw!")
    elif computer == 2:
        print("Computer wins!")
if player == 2:
    if computer == 0:
        print("Computer wins!")
    elif computer == 1:
        print("Player wins!")
    elif computer == 2:
        print("It's a draw!")
