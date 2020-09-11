import random


def main():
    print_rules()
    recursion = True
    board = reset_board()
    while recursion:
        print_linebreak()
        start = random.randint(1, 2)
        starting_player = select_player()[start % 2]
        print(f'(¯`·._.·Player {starting_player} starts!·._.·´¯)'.center(60))
        print_board(board)
        while True:
            current_player = select_player()[start % 2]
            player_move = select_move(current_player)
            if not place_move(player_move, current_player, board):
                print('Bzzzt! Wrong. This spot is already taken.')
                continue
            print_board(board)
            if check_for_win(board, current_player):
                print_linebreak()
                print(f'(¯`·._.·(¯`·._.· Player {current_player} wins!·._.·´¯)·._.·´¯)'.center(60))
                print_linebreak()
                break
            elif check_for_draw(board):
                print_linebreak()
                print("It's a draw! ¯\_(⊙︿⊙)_/¯".center(60))
                print_linebreak()
                break
            else:
                start += 1
        if check_recursion():
            board = reset_board()
            recursion = True
        else:
            print_linebreak()
            print(f"GOODBYE!".center(60))
            print_linebreak()
            recursion = False


def print_rules():
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


def print_linebreak():
    print('=' * 60)


def reset_board():
    return [' '] * 10


def print_board(game_board):
    print('+---+---+---+')
    print('| ' + game_board[7] + ' | ' + game_board[8] + ' | ' + game_board[9] + ' |')
    print('+---+---+---+')
    print('| ' + game_board[4] + ' | ' + game_board[5] + ' | ' + game_board[6] + ' |')
    print('+---+---+---+')
    print('| ' + game_board[1] + ' | ' + game_board[2] + ' | ' + game_board[3] + ' |')
    print('+---+---+---+')


def select_player():
    player1 = 'X'
    player2 = 'O'
    return player1, player2


def select_move(player_mark):
    while True:
        try:
            move_input = int(input(f'Player {player_mark} select your move:'))
        except ValueError:
            print('Bzzzt! Wrong. Insert only numbers 1-9.')
            continue
        else:
            if move_input not in range(1, 10):
                print('Bzzzt! Wrong. Insert only numbers 1-9.')
                continue
            else:
                return move_input


def place_move(position, player_mark, game_board):
    if game_board[position] != ' ':
        return False
    else:
        game_board[position] = player_mark
        return True


def check_horizontal_win(game_board, player):
    if game_board[1:4] == list(player * 3) \
            or game_board[4:7] == list(player * 3) \
            or game_board[7:10] == list(player * 3):
        return True
    else:
        return False


def check_vertical_win(game_board, player):
    if game_board[1:10:3] == list(player * 3) \
            or game_board[2:10:3] == list(player * 3) \
            or game_board[3:10:3] == list(player * 3):
        return True
    else:
        return False


def check_diagonal_win(game_board, player):
    if game_board[1:10:4] == list(player * 3) \
            or game_board[3:9:2] == list(player * 3):
        return True
    else:
        return False


def check_for_win(game_board, player):
    if check_horizontal_win(game_board, player) \
            or check_vertical_win(game_board, player) \
            or check_diagonal_win(game_board, player):
        return True
    else:
        return False


def check_for_draw(game_board):
    if ' ' not in game_board[1:10]:
        return True
    else:
        return False


def check_recursion():
    recursion_check = input('Do you want to play again? [Y/N]').lower()
    if recursion_check == 'y':
        return True
    else:
        return False


main()
