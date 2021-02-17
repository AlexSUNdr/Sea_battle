from game import Game, CellType


def draw_enemy(field, own):
    n = len(field) + 2
    m = len(field[0]) + 2
    for i in range(n):
        for j in range(m):
            if (i == 0 or i == n - 1) and (j == 0 or j == m - 1):
                print('+')
            elif (i == 0 or i == n - 1) or (j == 0 or j == m - 1):
                print('-')
            elif field[i][j] == CellType.SHIP:
                print('H')
            elif field[i][j] == CellType.EMPTY:
                print('o')
            elif field[i][j] == CellType.HIDDEN:
                print(' ')
            elif field[i][j] == CellType.SHIP_DAMAGED:
                print('X')
