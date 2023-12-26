import unittest
import numpy as np
from minesweeper.model.board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.width = 10
        self.height = 10
        self.mines = 10
        self.board = Board(self.width, self.height, self.mines)

    def test_initialization(self):
        self.assertEqual(self.board.width, self.width)
        self.assertEqual(self.board.height, self.height)
        self.assertEqual(self.board.mines, self.mines)

    def test_spread_mines(self):
        mines_count = np.sum(self.board._board == -1)
        self.assertEqual(mines_count, self.mines)

    def test_adjacent_mines_count(self):
        board = Board(3, 3, 2)
        _small_board = np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 0]])
        board._board = _small_board
        board._count_adjacent_mines(_small_board)

        expected_counts = np.array([[np.nan, 2, 1], [2, np.nan, 1], [1, 1, 1]])

        for x in range(3):
            for y in range(3):
                if _small_board[y, x] != -1:  # not a mine
                    self.assertEqual(_small_board[x, y], expected_counts[x, y])


if __name__ == "__main__":
    unittest.main()