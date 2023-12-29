from abc import ABC, abstractmethod


class IBoardPresenter(ABC):
    @abstractmethod
    def __init__(self, board):
        pass

    @abstractmethod
    def generate_view(self):
        pass
