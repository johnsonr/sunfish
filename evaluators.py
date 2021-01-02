from rule_based_eval import RuleBasedEvaluator
from pst_rules import createPstRules
from queenrules import noEarlyQueenAdvance
from playsharp_rules import developFast
import kingrules

# ClassicalEvaluator
# Tarrasch style
ConservativeEvaluator = RuleBasedEvaluator([
    createPstRules(piece={'P': 100, 'N': 300, 'B': 310,
                          'R': 500, 'Q': 900, 'K': 60000}),
    kingrules.mustBeAbleToCastle,
    kingrules.noEarlyKingMoves,
    kingrules.castleKingside(40),
    kingrules.castleQueenside,
    noEarlyQueenAdvance
]
)

MorphyEvaluator = RuleBasedEvaluator([
    createPstRules(piece={'P': 100, 'N': 300, 'B': 310,
                          'R': 500, 'Q': 900, 'K': 60000}),
    kingrules.mustBeAbleToCastle,
    kingrules.noEarlyKingMoves,
    kingrules.castleKingside(40),
    kingrules.castleQueenside,
    developFast(110),
]
)
