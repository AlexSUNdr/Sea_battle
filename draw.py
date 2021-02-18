import game

from os import system


def ask_user_name():
    clear_screen()
    print("Enter your name, please:")


def clear_screen():
    system("clear")
    draw_header()


def draw_header():
    print('#######################################')
    print('#        WELCOME TO SEA BATTLE        #')
    print('#######################################')
    print()


def draw_cell(cell):
    if cell == game.CellType.SHIP:
        print('#', end='')
    elif cell == game.CellType.EMPTY:
        print(' ', end='')
    elif cell == game.CellType.HIDDEN:
        print('.', end='')
    elif cell == game.CellType.SHIP_DAMAGED:
        print('X', end='')


def draw_row(row):
    for cell in row:
        draw_cell(cell)


def draw_field(field1, field2):
    clear_screen()

    n = len(field1)
    m = len(field1[0])
    print('+' + '-' * m + '+   +' + '-' * m + '+')
    for i in range(n):
        print('|', end='')
        draw_row(field1[i])
        print('|   |', end='')
        draw_row(field2[i])
        print('|')
    print('+' + '-' * m + '+   +' + '-' * m + '+')


def print_winner(winner):
    clear_screen()
    print(f"{winner.capitalize()} won!")
