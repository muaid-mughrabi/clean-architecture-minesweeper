import numpy as np
from scipy.signal import convolve2d
from minesweeper.model.interfaces.iboardgenerator import IBoardGenerator


class StandardBoardGenerator(IBoardGenerator):
    def generate(self, width, height, mines):
        board = np.zeros((height, width), dtype=int)
        self._spread_mines(board, mines)
        self._count_adjacent_mines(board)
        return board, np.zeros_like(board, dtype=bool)

    def _spread_mines(self, board, mines):
        positions = np.arange(board.shape[1] * board.shape[0])
        mine_positions = np.random.choice(positions, size=mines, replace=False)
        x_coords, y_coords = np.unravel_index(mine_positions, board.shape)
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
