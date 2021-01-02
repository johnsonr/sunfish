from rule_based_eval import RuleBasedEvaluator
from queenrules import noEarlyQueenAdvance
import kingrules

# ClassicalEvaluator
# Tarrasch style
ConservativeEvaluator = RuleBasedEvaluator([
    kingrules.mustBeAbleToCastle,
    kingrules.noEarlyKingMoves,
    kingrules.castleKingside(40),
    kingrules.castleQueenside,
    noEarlyQueenAdvance
]
)
