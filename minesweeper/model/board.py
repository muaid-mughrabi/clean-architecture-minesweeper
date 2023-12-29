from .boardgenerator import StandardBoardGenerator
from .interfaces.iboard import IBoard
from .boardrevealer import SingleCellBoardRevealer


class Board(IBoard):
    def __init__(self, width=10, height=10, mines=10, generator=None, revealer=None):
        self.width = width
        self.height = height
        self.mines = mines
        self.generator = generator if generator else StandardBoardGenerator()
        self.board, self.mask = self.generator.generate(width, height, mines)
        self._revealer = revealer if revealer else SingleCellBoardRevealer(self)

    def reveal_cell(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.mask[y, x] = True
            return self.board[y, x]
        else:
            # Coordinates are out of bounds, raise an exception
            raise IndexError(f"Coordinates ({x}, {y}) are out of board boundaries.")

    def reveal(self, x, y):
        return self._revealer.reveal(x, y)
