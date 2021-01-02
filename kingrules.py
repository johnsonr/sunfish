from rule_based_eval import GameStage
from piece import G1, C1, render


def noEarlyKingMoves(params):
    # No early king moves except castling

    if params.pieceMoved == "K" and params.gameStage == GameStage.Opening and params.toSquare != G1:
        # print("Early king move to ", render(params.toSquare))
        return -85
    return 0


def castleKingside(boost):
    def f(params):
        if params.pieceMoved == "K" and params.gameStage == GameStage.Opening and params.toSquare == G1:
            # print("Early king move to ", render(params.toSquare))
            return boost
        return 0
    return f


def castleQueenside(params):
    if params.pieceMoved == "K" and params.gameStage == GameStage.Opening and params.toSquare == C1:
        # print("Early king move to ", render(params.toSquare))
        return 10
    return 0


def mustBeAbleToCastle(params):
    return 0


# kingside pawn structure
