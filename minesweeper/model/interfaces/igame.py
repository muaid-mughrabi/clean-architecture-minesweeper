from abc import ABC, abstractmethod


class IGame(ABC):
    @abstractmethod
    def detect_state(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def reveal(self, x, y):
        pass
