board_items = ['', '', '', '', '', '', '', '', '']
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
        ch = input('Please enter you desired character (0 or X): ')

        if ch not in ['0', 'X']:
            print('Please choose right option (0 or X)')

    if ch == 'X':
        return ('X', '0')
    else:
        return ('0', 'X')


# ===============================
# Main operation starts from here
while game_running:
    print_board()
    player1, player2 = choose_character_option()
    print(f'Your character: {player1}')
