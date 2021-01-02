from piece import toAlgebraic


def noEarlyQueenAdvance(params):
    if params.pieceMoved == 'Q':
        # print("white Queen moved to ", toAlgebraic(params.fromSquare))
        return -30

    if params.pieceMoved == 'q':
        raise Exception("Black piece moved!!!")
    return 0
