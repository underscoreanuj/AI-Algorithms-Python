import random

class CspQueens():
    def __init__(self, board_size):
        self.board_size = board_size
        self.board = [x for x in range(board_size)]

    def printBoard(self):
        print("\n\n**********************SOLUTION**********************\n")
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board[j] == i:
                    print("Q", end='\t')
                else:
                    print("*", end='\t')
            print("\n")
        print("\n****************************************************\n")

    def constraint(self, board, col):
        seen = set()
        for i in range(col):
            if board[i] in seen:
                return False
            seen.add(board[i])

        for i in range(col):
            x = board[i]
            for j in range(col):
                if j != i:
                    if board[j] == x - (i-j) or board[j] == x + (i-j):
                        return False
        
        return True

    def solve(self, board=None, col=0):
        if board is None:
            board = self.board
        
        if col == len(board) and self.constraint(board, col):
            self.board = board
            self.printBoard()
            return True

        for i in range(col, len(self.board)):
            for q in range(len(self.board)):
                board[i] = q
                if self.constraint(board, col):
                    if self.solve(board, col+1):
                        if col > 1:
                            return True
                        else:
                            return False



problem = CspQueens(4)
problem.solve()
# problem.printBoard()
