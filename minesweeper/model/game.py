from minesweeper.model.board import Board
from minesweeper.model.constants import MINE_VALUE
from minesweeper.model.interfaces.igame import IGame


class Game(IGame):
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = mines
        self.board = Board(width, height, mines)
        self.game_over = False
        self.win = False

    def start(self):
        self.board = Board(self.width, self.height, self.mines)
        self.game_over = False
        self.win = False

    def detect_state(self):
        if self.game_over:
            return "Lost" if not self.win else "Won"
        elif all(
            (cell == MINE_VALUE or mask)
            for cell, mask in zip(self.board.board.flat, self.board.mask.flat)
        ):
            self.win = True
            self.game_over = True
            return "Won"
        else:
            return "Ongoing"

    def reveal(self, x, y):
        if self.game_over:
            return
        result = self.board.reveal(x, y)
        if result == MINE_VALUE:  # Hit a mine
            self.game_over = True
            self.win = False
        elif self.detect_state() == "Won":  # Check if all non-mine cells are revealed
            self.game_over = True
            self.win = True
        return result
