import controller

from random import randint


class Game:
    def __init__(self, height, width, user_name, fill_randomly=True):
        self.user_name = user_name

        self.height = height
        self.width = width

        self.player_field = GameField(height, width)
        self.computer_field = GameField(height, width)

        self.player_left = GameField.calculate_sum(GameField.calculate_max_ship_length(height, width))
        self.computer_left = self.player_left

        self.computer_field.fill_randomly()

        if fill_randomly:
            self.player_field.fill_randomly()
        else:
            self.player_field.fill_manually()

    def computer_move(self):
        empties = []
        for i in range(self.height):
            for j in range(self.width):
                if self.player_field.shown[i][j] == CellType.HIDDEN:
                    empties.append((i, j))
        x, y = empties[randint(0, len(empties) - 1)]
        if self.player_field.real[x][y] == CellType.SHIP:
            self.player_field.shown[x][y] = CellType.SHIP
            self.player_field.real[x][y] = CellType.SHIP_DAMAGED
            self.computer_left -= 1
            return True
        else:
            self.player_field.real[x][y] = CellType.HIDDEN
            self.player_field.shown[x][y] = CellType.EMPTY
            return False

    def player_move(self):
        x, y = controller.get_coordinates(self.user_name)
        if self.computer_field.real[x][y] == CellType.SHIP:
            self.computer_field.shown[x][y] = CellType.SHIP
            self.computer_field.real[x][y] = CellType.SHIP_DAMAGED
            self.player_left -= 1
            return True
        else:
            self.computer_field.shown[x][y] = CellType.EMPTY
            return False

    def check_win(self):
        if self.player_left == 0 or self.computer_left == 0:
            return True


def save_game(game):
    pass  # TODO


def load_game(save):
    pass  # TODO


class GameField:
    def __init__(self, height, width):
        self.height = height
        self.width = width

        self.shown = GameField._initialize_field(height, width, CellType.HIDDEN)
        self.real = GameField._initialize_field(height, width, CellType.EMPTY)

    def fill_randomly(self):
        max_ship_length = GameField.calculate_max_ship_length(self.height, self.width)
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
    def calculate_sum(k):
        result = 0
        for i in range(1, k + 1):
            result += i * (k - i + 1)
        return result

    @staticmethod
    def calculate_max_ship_length(height, width):
        optimal = 1

        for i in range(1, max(height, width) + 1):
            if GameField.calculate_sum(i) > height * width * 0.2:
                break
            optimal = i

        return optimal

    @staticmethod
    def _check_around(field, x, y):
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if x + dx < 0 or y + dy < 0:
                    continue
                if x + dx >= len(field) or y + dy >= len(field[0]):
                    continue
                if field[x + dx][y + dy] == CellType.SHIP:
                    return False
        return True

    @staticmethod
    def _check_placement(field, x, y, length, orientation):
        if orientation == 0:
            if x + length - 1 >= len(field):
                return False

            for i in range(x, x + length):
                if not GameField._check_around(field, i, y):
                    return False

            return True
        else:
            if y + length - 1 >= len(field[0]):
                return False

            for j in range(y, y + length):
                if not GameField._check_around(field, x, j):
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
    SHIP_DAMAGED = 4
