import os
import sys
import math
import curses
import argparse


def play(UserName):
    print('Nice start\n')



seabattle_str = '#######################################\n' \
             + '#        WELCOME TO SEA BATTLE        #\n' \
             + '#######################################\n\n'
player_name = 'Please enter your nickname: '
instructions_str = '\nPress p to play a new game.\nPress q to quit.'

# Display instructions
os.system('cls' if os.name == 'nt' else 'clear')
print(seabattle_str + instructions_str)

# Get user input
c = input()
if c == 'q' or c == 'Q':
    # Quit the game
    print('Ok, next time\n')
    sys.exit()
elif c == 'p' or c == 'P':
    # Enter username
    print(player_name)
    UserName = input()
            
    # Start new game
    play(UserName)


