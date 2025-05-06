def valid_move(position, board):
    return position in range(1, 10) and board.cells[position - 1] not in ['X', 'O']

def clean_input(input_str):
    try:
        return int(input_str.strip())
    except ValueError:
        return -1

def available_moves(board):
    for i, cell in enumerate(board.cells):
        if cell not in ['X', 'O']:
            yield i + 1