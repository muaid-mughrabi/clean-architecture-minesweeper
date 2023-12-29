import numpy as np

from minesweeper.view.interfaces.ipresenter import IBoardPresenter


class SimpleBoardPresenter(IBoardPresenter):
    def __init__(self, board):
        self.board = board

    def generate_view(self):
        x_array = np.full(self.board.board.shape, "x")

        # Use np.where to select 'x' for False and the corresponding value for True in the mask
        result = np.where(self.board.mask, self.board.board, x_array)

        return result
