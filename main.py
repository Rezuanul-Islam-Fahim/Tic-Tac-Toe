board_items = ['x', 'o', 'x', 'o', 'x', 'o', 'o', 'x', 'x']


def print_board():
    print(board_items[6] + '|' + board_items[7] + '|' + board_items[8])
    print(board_items[3] + '|' + board_items[4] + '|' + board_items[5])
    print(board_items[0] + '|' + board_items[1] + '|' + board_items[2])


print_board()
