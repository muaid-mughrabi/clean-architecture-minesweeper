from abc import ABC, abstractmethod


class IBoard(ABC):
    @abstractmethod
    def generate(self, width, height, mines):
        pass

    @abstractmethod
    def reveal(self, x, y):
        pass
