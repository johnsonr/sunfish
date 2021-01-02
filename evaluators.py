from rule_based_eval import RuleBasedEvaluator
from queenrules import noEarlyQueenAdvance
from kingrules import mustBeAbleToCastle, noEarlyKingMoves

DefaultEvaluator = RuleBasedEvaluator([
    mustBeAbleToCastle,
    noEarlyKingMoves,
    noEarlyQueenAdvance
]
)
