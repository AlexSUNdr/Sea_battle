from game import Game, CellType


def draw(field):
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == CellType.SHIP:

