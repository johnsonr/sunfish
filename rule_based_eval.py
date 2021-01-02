from evaluator import Evaluator

from collections import namedtuple
import enum


class GameStage(enum.Enum):
    Opening = 1
    Middlegame = 2
    Endgame = 3


# A rule is a function taking position and move, producing a delta to the previous score
# The aim is to see if the move makes the position better or worse for the mover
RuleParams = namedtuple(
    "RuleParams", "pos move fromSquare toSquare pieceMoved destinationSquareOccupant gameStage")

# Rul param is game stage to rule list


class RuleBasedEvaluator(Evaluator):
    # Evaluator using rules

    terminalsSeen = 0

    gameStageRules = []

    generalRules = []

    def __init__(self, generalRules, gameStageRules):
        self.generalRules = generalRules
        self.gameStageRules = gameStageRules

    def score(self, pos, move):
        self.terminalsSeen = self.terminalsSeen + 1
        score = 0

        fromSquare, toSquare = move
        pieceMoved, destinationSquareOccupant = pos.board[fromSquare], pos.board[toSquare]

        ##print(i, j, pieceMoved, destinationSquareOccupant)

        # Apply rules
        delta = 0
        gameStage = GameStage.Opening
        if pos.half_moves > 18:
            gameStage = GameStage.Middlegame
        if pos.half_moves > 80:
            gameStage = GameStage.Endgame
        params = RuleParams(pos, move, fromSquare, toSquare, pieceMoved,
                            destinationSquareOccupant, gameStage)

        for rule in self.generalRules:
            delta += rule(params)

        for stage, stageRules in self.gameStageRules.items():
            if gameStage == stage:
                for rule in stageRules:
                    delta += rule(params)
        # print("Delta from {0} rules is {1}".format(len(self.rules), delta))
        score += delta

        return score

    def terminals(self):
        return self.terminalsSeen
