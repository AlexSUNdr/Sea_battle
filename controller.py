import draw
import game


def start_game(height=10, width=10, save=None):
    draw.ask_user_name()
    user_name = input()

    if save is not None:
        sea = game.load_game(save)
    else:
        sea = game.Game(height, width, user_name)

    draw.draw_field(sea.computer_field.shown, sea.player_field.real)

    winner = None

    while winner is None:
        result = sea.player_move()
        while not sea.check_win() and result:
            draw.draw_field(sea.computer_field.shown, sea.player_field.real)
            result = sea.player_move()
        if sea.check_win():
            winner = "player"
        draw.draw_field(sea.computer_field.shown, sea.player_field.real)

        result = sea.computer_move()
        while not sea.check_win() and result:
            draw.draw_field(sea.computer_field.shown, sea.player_field.real)
            result = sea.computer_move()
        if sea.check_win():
            winner = "computer"
        draw.draw_field(sea.computer_field.shown, sea.player_field.real)

    draw.print_winner(winner)


def get_coordinates(user_name):
    print(f"{user_name}, enter coordinates to shoot:")
    x, y = map(int, input().split())
    return x - 1, y - 1
