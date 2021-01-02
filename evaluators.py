from rule_based_eval import RuleBasedEvaluator, pstRule
from queenrules import noEarlyQueenAdvance
import kingrules

# ClassicalEvaluator
# Tarrasch style
ConservativeEvaluator = RuleBasedEvaluator([
    pstRule,
    kingrules.mustBeAbleToCastle,
    kingrules.noEarlyKingMoves,
    kingrules.castleKingside(40),
    kingrules.castleQueenside,
    noEarlyQueenAdvance
]
)
