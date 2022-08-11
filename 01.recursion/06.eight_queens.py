def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def can_place_queen(row, col, rows, cols, left_diags, right_diags):
    if row in rows:
      return False
    if col in cols:
        return False
    if (row - col) in left_diags:
        return False
    if (row + col) in right_diags:
        return False

    return True  


def set_queen(row, col, board, rows, cols, left_diags, right_diags):
    board[row][col] = '*'
    rows.add(row)
    cols.add(col)
    left_diags.add(row - col)
    right_diags.add(row + col)


def remove_queen(row, col, board, rows, cols, left_diags, right_diags):
    board[row][col] = '-'
    rows.remove(row)
    cols.remove(col)
    left_diags.remove(row - col)
    right_diags.remove(row + col)


def place_queens(row, board, rows, cols, left_diags, right_diags):
    if (row == 8):
        print_board(board)
        return   

    for col in range(8):
        if can_place_queen(row, col, rows, cols, left_diags, right_diags):
            set_queen(row, col, board, rows, cols, left_diags, right_diags)
            place_queens(row + 1, board, rows, cols, left_diags, right_diags)
            remove_queen(row, col, board, rows, cols, left_diags, right_diags)

n = 8
board = []
[board.append(['-'] * n) for _ in range(8)]

place_queens(0, board, set(), set(), set(), set())

