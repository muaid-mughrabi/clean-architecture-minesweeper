from abc import ABC, abstractmethod


class IBoard(ABC):
    @abstractmethod
    def reveal(self, x, y):
        pass
