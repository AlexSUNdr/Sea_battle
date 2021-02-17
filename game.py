from random import randint


class Game:
    def __init__(self, height, width, user_name, fill_randomly=True):
        self.user_name = user_name

        self.player_field = GameField(height, width)
        self.computer_field = GameField(height, width)

        self.computer_field.fill_randomly()

        if fill_randomly:
            self.player_field.fill_randomly()
        else:
            self.player_field.fill_manually()


def save_game(game):
    pass  # TODO


def load_game():
    pass  # TODO


class GameField:
    def __init__(self, height, width):
        self.height = height
        self.width = width

        self.shown = GameField._initialize_field(height, width, CellType.HIDDEN)
        self.real = GameField._initialize_field(height, width, CellType.EMPTY)

    def fill_randomly(self):
        max_ship_length = GameField._calculate_max_ship_length(self.height, self.width)
        for ship_len in range(max_ship_length, 0, -1):
            for _ in range(max_ship_length - ship_len + 1):
                while True:
                    x = randint(0, self.height - 1)
                    y = randint(0, self.width - 1)
                    orientation = randint(0, 1)

                    if GameField._check_placement(self.real, x, y, ship_len, orientation):
                        GameField._place(self.real, x, y, ship_len, orientation)
                        break

    def fill_manually(self):
        pass  # TODO

    @staticmethod
    def _initialize_field(height, width, cell_type):
        return [[cell_type for _ in range(width)] for _ in range(height)]

    @staticmethod
    def _calculate_max_ship_length(height, width):
        def calculate_sum(k):
            result = 0
            for i in range(1, k + 1):
                result += i * (k - i + 1)
            return result

        optimal = 1

        for i in range(1, max(height, width) + 1):
            if calculate_sum(i) > height * width * 0.2:
                break
            optimal = i

        return optimal

    @staticmethod
    def _check_placement(field, x, y, length, orientation):
        if orientation == 0:
            if x + length - 1 >= len(field):
                return False

            for i in range(x, x + length):
                if field[i][y] != CellType.EMPTY:
                    return False

            return True
        else:
            if y + length - 1 >= len(field[0]):
                return False

            for j in range(y, y + length):
                if field[x][j] != CellType.EMPTY:
                    return False

            return True

    @staticmethod
    def _place(field, x, y, length, orientation):
        if orientation == 0:
            for i in range(x, x + length):
                field[i][y] = CellType.SHIP
        else:
            for j in range(y, y + length):
                field[x][j] = CellType.SHIP


class CellType:
    HIDDEN = 1
    EMPTY = 2
    SHIP = 3
