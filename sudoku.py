import copy

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

def solve(prev_board, row=0, col=0):
    board = copy.deepcopy(prev_board)
    next_row, next_col = next_row_col(row, col)

    # if the space is blank, we need to solve for it
    if board[row][col] == " ":
        # numbers that haven't been tried yet
        valid_nums = ['1','2','3','4','5','6','7','8','9']

        # do while loop
        while True:
            if len(valid_nums) == 0:
                if row == 0 and col == 0:
                    print("unable to solve board")
                    exit()
                return
            num_to_try = valid_nums.pop()
            if is_value_at_position_valid(board, num_to_try, row, col):
                board[row][col] = num_to_try
                print_board(board)

                # if we just finished solving for the last row and column, print the board
                if row == 8 and col == 8:
                    print("board solved")
                    exit()
                else:
                    solve(board, next_row, next_col)
    else:
        print("skipping", row, ", ", col)
        solve(board, next_row, next_col)


def is_value_at_position_valid(board, value, row, col):
    row_col = "(" + str(row) + "," + str(col) + ")"
    if value in numbers_in_row(board, row):
        print(row_col, value, "in row")
        return False
    if value in numbers_in_col(board, col):
        print(row_col, value, "in col")
        return False
    if value in numbers_in_block(board, row, col):
        print(row_col, value, "in block")
        return False
    print(row_col, value, "is valid")
    return True


def numbers_in_row(board, row):
    return board[row]
def numbers_in_col(board, col):
    return [board[x][col] for x in range(9)]
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
print_board(board)
solve(board)
