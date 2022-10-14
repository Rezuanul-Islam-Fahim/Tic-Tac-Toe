from os import system


board_items = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
game_running = True


# =============================
# Function for printing the board
def print_board():
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

    if ch == 'X':
        return ('X', '0')
    else:
        return ('0', 'X')


# ==========================
# Function for adding char to a position
def update_board(pos, player, board_items):
    board_items[pos-1] = player
    return board_items


# ===========================
# Function for validating position
def validate_get_position():
    pos = -1

    while pos not in range(1, 10):
        try:
            pos = int(input('\nEnter a position: '))
        except:
            print('Please enter a valid input number between (1 - 9)')
            pos = None

        if not pos == None and pos not in range(1, 10):
            print('Please enter a position between (1 - 9)')

    return pos


# ===============================
# Main operation starts from here
while game_running:
    print('\n')
    print_board()
    player1, player2 = choose_character_option()
    system('cls')
    print(f'\n======= You have choosen: {player1} ========')
    print('Your turn first\n')
    board_ongoing = True
    steps = 0

    while board_ongoing:
        print_board()
        pos = validate_get_position()
        board_items = update_board(
            pos,
            player1 if steps % 2 == 0 else player2,
            board_items
        )
        system('cls')
        print_board()
        board_ongoing = False
        game_running = False
