import numpy as np
from scipy.signal import convolve2d
from .interfaces.iboard import IBoard
from .board_revealer import SingleCellBoardRevealer


class Board(IBoard):
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = mines
        self._board = self.generate(width, height, mines)
        self._mask = np.zeros_like(self._board, dtype=bool)
        self._revealer = SingleCellBoardRevealer(self)

    def generate(self, width, height, mines):
        board = np.zeros((height, width), dtype=int)

        self._spread_mines(board, mines)
        self._count_adjacent_mines(board)

        return board

    def _spread_mines(self, board, mines):
        positions = np.arange(self.width * self.height)
        mine_positions = np.random.choice(positions, size=mines, replace=False)
        x_coords, y_coords = np.unravel_index(mine_positions, (self.height, self.width))
        board[y_coords, x_coords] = -1

    def _count_adjacent_mines(self, board):
        # Create a temporary board to mark mines as 1
        temp_board = np.zeros_like(board)
        temp_board[board == -1] = 1  # Mark mines

        # Define the convolution kernel
        kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])

        # Apply convolution to count adjacent mines
        adjacent_mines = convolve2d(
            temp_board, kernel, mode="same", boundary="fill", fillvalue=0
        )

        # Update the board with the count of adjacent mines
        # Only update non-mine cells
        non_mine_cells = board != -1
        board[non_mine_cells] += adjacent_mines[non_mine_cells]

    def reveal_cell(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self._mask[y, x] = True
            return self._board[y, x]
        else:
            # Coordinates are out of bounds, raise an exception
            raise IndexError(f"Coordinates ({x}, {y}) are out of board boundaries.")

    def reveal(self, x, y):
        return self._revealer.reveal(x, y)
