from piece import B1, C1, F1, G1, E2, D2, E4, D4
from rule_based_eval import GameStage

# Seek sharp positions - open files

# Seek threats

# what can we look for in enemy position?


def developFast(boost):
    def f(params):
        if params.gameStage == GameStage.Opening:
            if params.fromSquare in [B1, C1, F1, G1, D2, E2]:
                return boost
        return 0
    return f


def occupyCenter(boost):
    def f(params):
        if params.gameStage == GameStage.Opening:
            if params.toSquare in [D4, E4]:
                return boost
        return 0
    return f
