"""
Tania Akthar
Project 2, Part 2 (switch_player(self))
Oct 24, 2025
"""

import unittest
from connect4 import Connect4

class TestConnect4(unittest.TestCase):

    def setUp(self):
        self.game = Connect4()

    def test_switch_player(self):
        self.assertEqual(self.game.current_player, 'X')
        self.game.switch_player()
        self.assertEqual(self.game.current_player, 'O')
        self.game.switch_player()
        self.assertEqual(self.game.current_player, 'X')

    def test_horizontal_win(self):
        for c in range(4):
            self.game.board[5][c] = 'X'
        self.assertTrue(self.game.check_winner('X'))

    def test_vertical_win(self):
        for r in range(4):
            self.game.board[r][2] = 'O'
        self.assertTrue(self.game.check_winner('O'))

    def test_diagonal_win(self):
        self.game.board[5][0] = 'X'
        self.game.board[4][1] = 'X'
        self.game.board[3][2] = 'X'
        self.game.board[2][3] = 'X'
        self.assertTrue(self.game.check_winner('X'))

    def test_no_win(self):
        self.game.board[5][0] = 'X'
        self.game.board[5][1] = 'O'
        self.game.board[5][2] = 'X'
        self.assertFalse(self.game.check_winner('X'))

    def test_drop_chip(self):
        result = self.game.drop_chip(3)
        self.assertTrue(result)
        self.assertEqual(self.game.board[5][3], 'X')

    def test_full_column(self):
        for _ in range(6):
            self.game.drop_chip(1)
            self.game.switch_player()
        result = self.game.drop_chip(1)
        self.assertFalse(result)

    def test_invalid_column(self):
        self.assertFalse(self.game.drop_chip(-1))
        self.assertFalse(self.game.drop_chip(8))

if __name__ == "__main__":
    unittest.main()

