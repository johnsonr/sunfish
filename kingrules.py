from rule_based_eval import GameStage
from piece import G1, render


def noEarlyKingMoves(params):
    if params.pieceMoved == "K" and params.gameStage == GameStage.Opening and params.toSquare != G1:
        # print("Early king move to ", render(params.toSquare))
        return -85
    return 0


def mustBeAbleToCastle(params):
    return 0


# kingside pawn structure
