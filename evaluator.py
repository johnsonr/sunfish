from abc import ABC, abstractmethod


class Evaluator(ABC):

    @abstractmethod
    def score(pos, move):
        pass

    @abstractmethod
    def terminals(self):
        pass
