import copy

class Board:
    def __init__(self, filename):
        self.empty_board = [[0 for x in range(9)] for y in range(9)]
        self.solved_board = copy.deepcopy(self.empty_board)
        self.load(filename)
        self.print_board(self.empty_board)


    def load(self, filename):
        file = open(filename, "r")
        for i in range(9):
            for j in range(9):
                self.empty_board[i][j] = file.read(1)
            file.read(1)


    def print_board(self, board):
        for i in range(9):
            print(self.board[i])


    def solve(self):
        pass


    def __solve(self, row, col):
        pass


