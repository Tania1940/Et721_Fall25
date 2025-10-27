"""
Tania Akthar
Oct 24, 2025
Project 2 - part 2
"""

class Connect4:

    def __init__(self):
        self.rows = 6
        self.cols = 7
        self.board = []
        for r in range(self.rows):
            self.board.append([' ']*self.cols)
        self.current_player = 'X'

    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def drop_chip(self, col):
        if col < 0 or col >= self.cols:
            return False
        for r in range(self.rows-1, -1, -1):
            if self.board[r][col] == ' ':
                self.board[r][col] = self.current_player
                return True
        return False

    def check_winner(self, chip):
        for r in range(self.rows):
            for c in range(self.cols-3):
                if self.board[r][c] == chip and self.board[r][c+1] == chip and \
                   self.board[r][c+2] == chip and self.board[r][c+3] == chip:
                    return True

        for r in range(self.rows-3):
            for c in range(self.cols):
                if self.board[r][c] == chip and self.board[r+1][c] == chip and \
                   self.board[r+2][c] == chip and self.board[r+3][c] == chip:
                    return True

        for r in range(self.rows-3):
            for c in range(self.cols-3):
                if self.board[r][c] == chip and self.board[r+1][c+1] == chip and \
                   self.board[r+2][c+2] == chip and self.board[r+3][c+3] == chip:
                    return True

        for r in range(3, self.rows):
            for c in range(self.cols-3):
                if self.board[r][c] == chip and self.board[r-1][c+1] == chip and \
                   self.board[r-2][c+2] == chip and self.board[r-3][c+3] == chip:
                    return True
        return False
