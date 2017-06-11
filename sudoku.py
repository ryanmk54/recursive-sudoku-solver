def load(filename):
    file = open(filename, "r")

    board = [[0 for x in range(9)] for y in range(9)]
    for i in range(9):
        for j in range(9):
            board[i][j] = file.read(1)
        file.read(1)
    return board


def print_board(board):
    for i in range(9):
        print(board[i])

def solve(board, row=0, col=0):
    print("solving", row, ", ", col)
    print_board(board)

    # if the space is blank, we need to solve for it
    if board[row][col] == " ":
        value_at_position = solve_position(board, row, col)
        if value_at_position:
            board[row][col] = value_at_position
        else:
            return

    # if we just finished solving for the last row and column, print the board
    if row == 8 and col == 8:
        print_board(board)
        exit
    # otherwise, solve for the next spot
    else:
        next_row, next_col = next_row_col(row, col)
        solve(board, next_row, next_col)


def solve_position(board, row, col):
    valid_nums = [1,2,3,4,5,6,7,8,9]

    while True:
        if len(valid_nums) == 0:
            return False

        num_to_try = valid_nums.pop()
        if is_value_at_position_valid(board, num_to_try, row, col):
            return num_to_try


def is_value_at_position_valid(board, value, row, col):
    if value in numbers_in_row(board, row):
        return False
    if value in numbers_in_col(board, col):
        return False
    if value in numbers_in_block(board, row, col):
        return False
    return True


def numbers_in_row(board, row):
    return board[row]
def numbers_in_col(board, col):
    return [board[col] for x in range(9)]
def numbers_in_block(board, row, col):
    row_block_num = row // 3
    col_block_num = col // 3
    return [
            board[row_block_num*3][col_block_num*3],
            board[row_block_num*3 + 1][col_block_num*3],
            board[row_block_num*3 + 2][col_block_num*3],
            board[row_block_num*3][col_block_num*3 + 1],
            board[row_block_num*3 + 1][col_block_num*3 + 1],
            board[row_block_num*3 + 2][col_block_num*3 + 1],
            board[row_block_num*3][col_block_num*3 + 2],
            board[row_block_num*3 + 1][col_block_num*3 + 2],
            board[row_block_num*3 + 2][col_block_num*3 + 2]
           ]

def next_row_col(row, col):
    col += 1
    if col == 9:
        row += 1
        col = 0
    return row, col


board = load("1.board")
solve(board)
