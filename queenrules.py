from rule_based_eval import GameStage


def earlyQueenAdvance(delta):
    def f(params):
        if params.gameStage != GameStage.Opening:
            # print("too late to worry about queen advance at ", params.pos.half_moves)
            return 0

        if params.pieceMoved == 'Q':
            # print("white Queen moved to ", toAlgebraic(params.fromSquare))
            return delta

        if params.pieceMoved == 'q':
            raise Exception("Black piece moved!!!")
        return 0
    return f
