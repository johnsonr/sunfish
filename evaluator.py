from abc import ABC, abstractmethod

# Implemented by classes that can evaluate moves from a given position


class Evaluator(ABC):

    @abstractmethod
    def score(pos, move):
        pass

    @abstractmethod
    def terminals(self):
        pass
