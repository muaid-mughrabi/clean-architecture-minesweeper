import unittest
from minesweeper.model.board_revealer import SingleCellBoardRevealer
from minesweeper.model.board import Board


class TestBoardRevealer(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.revealer = SingleCellBoardRevealer(self.board)

    def test_reveal_empty_cell(self):
        x, y = 2, 2
        self.board._board[y, x] = 0
        result = self.revealer.reveal(x, y)
        self.assertTrue(self.board._mask[y, x])
        self.assertEqual(result, 0, "Revealed value should be 0 for an empty cell")

    def test_reveal_mine(self):
        x, y = 1, 1
        self.board._board[y, x] = -1  # Place a mine
        result = self.revealer.reveal(x, y)
        self.assertTrue(self.board._mask[y, x])
        self.assertEqual(result, -1, "Revealed value should be -1 for a mine")

    def test_reveal_out_of_bounds(self):
        out_of_bounds_x, out_of_bounds_y = (
            self.board.width,
            self.board.height,
        )  # One past the edge
        with self.assertRaises(IndexError):
            self.revealer.reveal(out_of_bounds_x, out_of_bounds_y)


if __name__ == "__main__":
    unittest.main()
