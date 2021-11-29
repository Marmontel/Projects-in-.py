# Objective: Create a program that makes the computer play JOKENPO with you

import time 
import random 
print('='*11, 'JOKENPÔ', '='*11, '\n')
print('''YOUR OPTIONS:
{ 0 } STONE
{ 1 } PAPER
{ 2 } SCISSORS
''')
computer = random.randint(0, 2)
player = int(input('Choose your element: '))
if player >= 3:
    print('OPTION INVALID! TRY AGAIN.')
    exit()
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÔ!!!')
print('~='*20)
time.sleep(1)
print('RESULT:')
if player == computer:
    print('The computer opted for the same element! DRAW')
elif player == 0 and computer == 1:
    print('The computer played PAPER. \nPlayer played STONE')
    print('=-'*20)
    print('YOU LOSE')
elif player == 1 and computer == 2:
    print('The computer played SCISSORS.\nPlayer played PAPER.')
    print('=-'*20)
    print('YOU LOSE')
elif player == 2 and computer == 0:
    print('The computer played STONE./nPlayer played SCISSORS.')
    print('=-')
    print('YOU LOSE')
elif player == 0 and computer == 1:
    print('The computer played SCISSORS.\nPlayer played STONE.')
    print('=-')
    print('YOU WIN')
elif player == 1 and computer == 0:
    print('The computer player STONE.\nPlayer played PAPER.')
    print('=-'*20)
    print('YOU WIN')
elif player == 2 and computer == 1:
    print('The computer played PAPER.\nPlayer played SCISSORS.')
    print('=-'*20)
    print('YOU WIN')
else: 
    print('INVALID OPTION! TRY AGAIN.')
