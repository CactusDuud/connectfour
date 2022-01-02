# Part 2 of 5: HumanVHuman Connect Four
# Sage Mahmud - 11686625
# ICS 32 Winter 2019
# Project #2: Send Me On My Way

from connectfour import connectfour_shared

RED = connectfour_shared.RED
YELLOW = connectfour_shared.YELLOW


def _start_game():
    game_over = False
    game_state = connectfour_shared.make_new_game()
    while not game_over:
        connectfour_shared.print_board(game_state)
        if game_state.turn == RED:
            print('RED\'s turn')
        elif game_state.turn == YELLOW:
            print('YELLOW\'s turn')

        game_state = connectfour_shared.do_turn(game_state)
        print()
        game_over = connectfour_shared.declare_winner(game_state)


if __name__ == '__main__':
    _start_game()
    replay = input('Would you like to play again?\n'
                   'Type \"yes\" to play again\n'
                   '>>> '
                   ).lower()
    if replay.startswith('yes'):
        print('\n\n')
        _start_game()
