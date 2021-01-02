from rule_based_eval import GameStage
from piece import G1, C1, render


def earlyKingMoves(delta):
    # No early king moves except castling

    def f(params):
        if params.pieceMoved == "K" and params.gameStage == GameStage.Opening and params.toSquare != G1:
            # print("Early king move to ", render(params.toSquare))
            return delta
        return 0
    return f


def castleKingside(delta):
    def f(params):
        if params.pieceMoved == "K" and params.gameStage == GameStage.Opening and params.toSquare == G1:
            # print("Early king move to ", render(params.toSquare))
            return delta
        return 0
    return f


def castleQueenside(delta):
    def f(params):
        if params.pieceMoved == "K" and params.gameStage == GameStage.Opening and params.toSquare == C1:
            # print("Early king move to ", render(params.toSquare))
            return delta
        return 0
    return f


def unableToCastle(delta):

    def f(params):
        return 0
    return f


# kingside pawn structure
