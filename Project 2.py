import random


def main():
    print_rules()
    wanna_play_game = True
    board = reset_board()
    while wanna_play_game:
        turn = random.randint(1, 2)
        print_starting_player(player_by_turn(turn))
        print_board(board)

        game_in_progress = True
        while game_in_progress:
            current_player = player_by_turn(turn)
            player_move = select_move(current_player)
            if is_position_free(player_move, board):
                place_move(player_move, current_player, board)
            else:
                print_spot_taken()
                continue
            print_board(board)
            if is_winner(board, current_player):
                print_winner(current_player)
                break
            elif check_for_draw(board):
                print_draw()
                break
            else:
                turn += 1

        if user_wants_to_play_again():
            board = reset_board()
        else:
            print_goodbye()
            break


def print_rules() -> str:
    print('''                      WELCOME TO THE
      _____ ___ ___   _____ _   ___   _____ ___  ___ 
     |_   _|_ _/ __| |_   _/_\ / __| |_   _/ _ \| __|
       | |  | | (__    | |/ _ \ (__    | || (_) | _| 
       |_| |___\___|   |_/_/ \_\___|   |_| \___/|___|

    Use your numeric keyboard to select position of your move:
             GAME BOARD    ->   NUM KEYBOARD                                                 
            +---+---+---+      +---+---+---+                                                 
            | x |   |   |      | 7 | 8 | 9 |  
            +---+---+---+      +---+---+---+
            |   | O |   |      | 4 | 5 | 6 | 
            +---+---+---+      +---+---+---+
            |   | x | O |      | 1 | 2 | 3 | 
            +---+---+---+      +---+---+---+''')


def reset_board() -> list:
    return [' '] * 10


def print_board(game_board: list) -> str:
    print('+---+---+---+')
    print('| ' + game_board[7] + ' | ' + game_board[8] + ' | ' + game_board[9] + ' |')
    print('+---+---+---+')
    print('| ' + game_board[4] + ' | ' + game_board[5] + ' | ' + game_board[6] + ' |')
    print('+---+---+---+')
    print('| ' + game_board[1] + ' | ' + game_board[2] + ' | ' + game_board[3] + ' |')
    print('+---+---+---+')


def player_list() -> tuple:
    player1 = 'X'
    player2 = 'O'
    return player1, player2


def player_by_turn(turn: int) -> str:
    return player_list()[turn % 2]


def print_linebreak() -> str:
    print('=' * 60)


def decorator_add_linebreaks(func):
    def wrapper(*x):
        print_linebreak()
        func(*x)
        print_linebreak()
    return wrapper


@decorator_add_linebreaks
def print_starting_player(starting_player: str) -> str:
    print(f'(¯`·._.·Player {starting_player} starts!·._.·´¯)'.center(60))


def select_move(player_mark: str) -> int:
    while True:
        try:
            selected_move = int(input(f'Player {player_mark} select your move:'))
        except ValueError:
            print_incorrect_number()
            continue
        if selected_move not in range(1, 10):
            print_incorrect_number()
            continue
        else:
            return selected_move


def print_incorrect_number() -> str:
    print('Bzzzt! Wrong. Insert only numbers 1-9.')


def is_position_free(position: int, game_board: list) -> bool:
    return bool(game_board[position] == ' ')


def print_spot_taken() -> str:
    print('Bzzzt! Wrong. This spot is already taken.')


def place_move(position: int, player_mark: str, game_board: list):
    if is_position_free(position, game_board):
        game_board[position] = player_mark
    else:
        print_spot_taken()


def check_horizontal_win(game_board: list, player: str) -> bool:
    return game_board[1:4] == list(player * 3) \
            or game_board[4:7] == list(player * 3) \
            or game_board[7:10] == list(player * 3)


def check_vertical_win(game_board: list, player: str) -> bool:
    return game_board[1:10:3] == list(player * 3) \
            or game_board[2:10:3] == list(player * 3) \
            or game_board[3:10:3] == list(player * 3)


def check_diagonal_win(game_board: list, player: str) -> bool:
    return game_board[1:10:4] == list(player * 3) \
            or game_board[3:9:2] == list(player * 3)


def is_winner(game_board: list, player: str) -> bool:
    return check_horizontal_win(game_board, player) \
            or check_vertical_win(game_board, player) \
            or check_diagonal_win(game_board, player)


def check_for_draw(game_board: list) -> bool:
    return ' ' not in game_board[1:10]


def user_wants_to_play_again() -> bool:
    recursion_check = input('Do you want to play again? [Y/N]').lower()
    return recursion_check == 'y'


@decorator_add_linebreaks
def print_draw() -> str:
    print("It's a draw! ¯\_(⊙︿⊙)_/¯".center(60))


@decorator_add_linebreaks
def print_winner(current_player: str) -> str:
    print(f'(¯`·._.·(¯`·._.· Player {current_player} wins!·._.·´¯)·._.·´¯)'.center(60))


@decorator_add_linebreaks
def print_goodbye() -> str:
    print(f"GOODBYE!".center(60))


main()
