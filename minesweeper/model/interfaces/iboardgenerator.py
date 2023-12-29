from abc import ABC, abstractmethod


class IBoardGenerator(ABC):
    @abstractmethod
    def generate(self, width, height, mines):
        pass
