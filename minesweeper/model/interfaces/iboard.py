from abc import ABC, abstractmethod


class IBoard(ABC):
    @abstractmethod
    def generate(self, w, h):
        pass

    @abstractmethod
    def reveal(self, x, y):
        pass
