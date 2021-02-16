import os
import sys
import math
import curses
import argparse

def How_many_ships(height, width):
    V = height * width
    #waiting for bin_f from Tagir

def fill_by_yourself():
    print('By yourself\n')

def fill_automatically():
    print('Authomatically\n')

def Choose_type_of_filling():
    print('\nPress y to fill ships on sea field yourself.\nPress a to take automatically generated sea field')
    c = input()
    if c == 'y' or c == 'Y':
        fill_by_yourself()
    elif c == 'a' or c == 'A':
        fill_automatically() 

def play(UserName):
    V = 0
    while V < 25:
        print('Enter height of field')
        height = int(input())
        print('Enter width of field')
        width = int(input())
        V = height * width
        if V < 25:
            print('Your field is very small, enter another size of field\n\n')

    Choose_type_of_filling(height, width)

    ships = How_many_ships()
    

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



