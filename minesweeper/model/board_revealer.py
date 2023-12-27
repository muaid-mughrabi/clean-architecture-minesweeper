from .interfaces.iboardrevealer import IBoardRevealer


class SingleCellBoardRevealer(IBoardRevealer):
    def __init__(self, board):
        self.board = board
        self.width = board.width
        self.height = board.height

    def reveal(self, x, y):
        return self.board.reveal_cell(x, y)
