from piece import toAlgebraic


def noEarlyQueenAdvance(params):
    if params.pos.half_moves > 18:
        print("too late at ", params.pos.half_moves)
        return 0

    if params.pieceMoved == 'Q':
        # print("white Queen moved to ", toAlgebraic(params.fromSquare))
        return -30

    if params.pieceMoved == 'q':
        raise Exception("Black piece moved!!!")
    return 0
