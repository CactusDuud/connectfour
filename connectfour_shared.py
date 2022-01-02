# Part 4 of 5: Shared code for a Connect Four game
# Sage Mahmud - 11686625
# ICS 32 Winter 2019
# Project #2: Send Me On My Way

from connectfour import connectfour

NONE = connectfour.NONE
RED = connectfour.RED
YELLOW = connectfour.YELLOW
COLUMNS = connectfour.BOARD_COLUMNS
ROWS = connectfour.BOARD_ROWS


def declare_winner(game_state: connectfour.GameState) -> bool:
    """Reads the board and declares the winner"""
    if connectfour.winner(game_state) == NONE:
        return False
    elif connectfour.winner(game_state) == RED:
        print_board(game_state)
        print('Red wins! Good game!')
        return True
    elif connectfour.winner(game_state) == YELLOW:
        print_board(game_state)
        print('Yellow wins! Good game!')
        return True


def print_board(game_state: connectfour.GameState) -> None:
    """prints out the board"""
    board = game_state.board
    spacing = ' ' * (len(str(COLUMNS)) + 1)
    for col in range(0, COLUMNS):
        if col > 8:
            spacing = ' ' * len(str(COLUMNS))
        print(f'{col + 1}{spacing}', end='')
    print()
    for row in range(0, ROWS):
        for col in board:
            spacing = ' ' * (len(str(COLUMNS)) + 1)
            piece = col[row]
            if piece == NONE:
                piece = '.'
            elif piece == RED:
                piece = 'R'
            elif piece == YELLOW:
                piece = 'Y'

            if row == ROWS:
                print(f'{piece}')
            else:
                print(f'{piece}{spacing}', end='')
        print()


def do_turn(game_state: connectfour.GameState) -> connectfour.GameState:
    """facilitates a single turn"""
    print('Player may type:\n'
          '1. DROP (or just D) to drop one of their pieces onto the grid\n'
          '2. POP (or just P) to pop one of their pieces, removing it from the grid'
          )
    while True:
        user_in = input('>>> ').lower()
        if user_in.startswith('drop '):
            result = drop(game_state, int(user_in[5:]) - 1)
            if result:
                return result
        elif user_in.startswith('d ') or user_in.startswith('1 '):
            result = drop(game_state, int(user_in[2:]) - 1)
            if result:
                return result
        elif user_in.startswith('pop '):
            result = pop(game_state, int(user_in[4:]) - 1)
            if result:
                return result
        elif user_in.startswith('p ') or user_in.startswith('2 '):
            result = pop(game_state, int(user_in[2:]) - 1)
            if result:
                return result
        else:
            print('Input not recognized, please try again')


def drop(game_state: connectfour.GameState, col: int) -> connectfour.GameState or False:
    """attempts to drop a piece onto the board, in event of failure prints an error message and returns False"""
    try:
        return connectfour.drop(game_state, int(col))
    except ValueError:
        print(f'Invalid column number; please input a number between 1 and {COLUMNS}')
        return False
    except connectfour.InvalidMoveError:
        print('Invalid move; please select an empty column')
        return False


def pop(game_state: connectfour.GameState, col: int) -> connectfour.GameState or False:
    """attempts to pop a piece on the board, in event of failure prints an error message and returns False"""
    try:
        return connectfour.pop(game_state, col)
    except ValueError:
        print(f'Invalid column number; please input a number between 1 and {COLUMNS}')
    except connectfour.InvalidMoveError:
        print('Invalid move; players can only pop their own pieces from the bottom row')
    pass


def make_new_game() -> connectfour.GameState:
    """creates a new game"""
    return connectfour.new_game()
