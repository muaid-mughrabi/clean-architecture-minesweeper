from abc import ABC, abstractmethod


class IBoardRevealer(ABC):
    @abstractmethod
    def __init__(self, board):
        pass

    @abstractmethod
    def reveal(self, x, y):
        pass
