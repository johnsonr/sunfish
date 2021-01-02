from rule_based_eval import GameStage


def noEarlyKingMoves(params):
    if params.gameStage == GameStage.Opening:
        return -1
    return 0


def mustBeAbleToCastle(params):
    return 0


# kingside pawn structure
