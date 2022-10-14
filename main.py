from os import system


# =============================
# Function for printing the board
def print_board(board_items):
    print(board_items[6] + '|' + board_items[7] + '|' + board_items[8])
    print(board_items[3] + '|' + board_items[4] + '|' + board_items[5])
    print(board_items[0] + '|' + board_items[1] + '|' + board_items[2])


# ================================
# Function for selecting character
def choose_character_option():
    ch = ''

    while ch not in ['0', 'X']:
        ch = input('\nPlease enter you desired character (0 or X): ')

        if ch not in ['0', 'X']:
            print('Please choose right option (0 or X)')

    return ('X', '0') if ch == 'X' else ('0', 'X')


# ==========================
# Function for adding char to a position
def update_board(pos, player, board_items):
    board_items[pos-1] = player
    return board_items


# ===========================
# Function for validating position
def validate_get_position(steps, board_items):
    pos = 0

    while not (pos in range(1, 10) and board_items[pos-1] == '-'):
        try:
            pos = int(
                input(f'\nPlayer {1 if steps%2==0 else 2}, Enter a position: ')
            )
        except:
            print('Please enter a valid input number between (1 - 9)')
            pos = None

        if not (pos == None or pos in range(1, 10)):
            print('Please enter a position between (1 - 9)')
        elif not (pos == None or board_items[pos-1] == '-'):
            print(f'Position {pos} is already occupied')

    return pos


# ================================
# Function for getting match result
def get_match_result(steps, player1, player2):
    player_char = player1 if steps % 2 == 0 else player2
    player = 'Player 1' if steps % 2 == 0 else 'Player 2'

    if (board_items[0] == board_items[1] == board_items[2] == player_char or
        board_items[3] == board_items[4] == board_items[5] == player_char or
        board_items[6] == board_items[7] == board_items[8] == player_char or
        board_items[0] == board_items[3] == board_items[6] == player_char or
        board_items[1] == board_items[4] == board_items[7] == player_char or
        board_items[2] == board_items[5] == board_items[8] == player_char or
        board_items[0] == board_items[4] == board_items[8] == player_char or
            board_items[2] == board_items[4] == board_items[6] == player_char):
        print(
            f'=========================\n\t{player} wins\n=========================')
        return False
    elif steps == len(board_items) - 1:
        print('\n======= Match Draw ========')
        return False

    return True


# ============================
# Continue confirmation
def match_continiue_confirm():
    confirm = ''

    while confirm not in ['Y', 'N']:
        confirm = input('\nDo you want to continue (Y, N): ')

        if confirm not in ['Y', 'N']:
            print('Please enter a valid input')

    return True if confirm == 'Y' else False


# ===============================
# Main operation starts from here
while True:
    board_items = ['-']*9
    system('cls')
    print_board(board_items)
    player1, player2 = choose_character_option()
    system('cls')
    print(f'\n======= You have choosen: {player1} ========')
    print('Your turn first\n')
    steps = 0

    while True:
        if not steps == 0:
            system('cls')

        print_board(board_items)
        pos = validate_get_position(steps, board_items)
        board_items = update_board(
            pos,
            player1 if steps % 2 == 0 else player2,
            board_items
        )
        system('cls')
        print_board(board_items)

        if not get_match_result(steps, player1, player2):
            break

        steps += 1

    if not match_continiue_confirm():
        break
