"""
ET721 - Fall 2025
Unit Test Report - Part 2
Student: Tania Akthar
Method: switch_player(self)
"""

import unittest
from main import Connect4


class TestSwitchPlayer(unittest.TestCase):
    def test_switch_from_X_to_O(self):
        """Verify the player changes from X to O."""
        game = Connect4()
        game.current_player = 'X'
        game.switch_player()
        self.assertEqual(game.current_player, 'O')

    def test_switch_from_O_to_X(self):
        """Verify the player changes from O to X."""
        game = Connect4()
        game.current_player = 'O'
        game.switch_player()
        self.assertEqual(game.current_player, 'X')

    def test_multiple_switches(self):
        """Ensure switching twice returns to the original player."""
        game = Connect4()
        game.current_player = 'X'
        game.switch_player()  # becomes O
        game.switch_player()  # back to X
        self.assertEqual(game.current_player, 'X')


if __name__ == '__main__':
    unittest.main()

"""

Objective:
To confirm that the switch_player() function correctly alternates
the current_player attribute between 'X' and 'O' during gameplay.

Tests Conducted:
1. test_switch_from_X_to_O - Verified that 'X' changes to 'O'.
2. test_switch_from_O_to_X - Verified that 'O' changes to 'X'.
3. test_multiple_switches - Verified that switching twice restores the original player.

Results:
All tests executed successfully with no failures.
The switch_player() method behaves as expected, ensuring accurate
player alternation in the Connect4 game logic.

Conclusion:
The function is reliable and functions correctly under multiple consecutive switches.
-------------------------------------------------------------
"""
