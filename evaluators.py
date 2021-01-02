from rule_based_eval import RuleBasedEvaluator, GameStage
from pst_rules import createPstRules
from playsharp_rules import developFast
import kingrules
import queenrules

# ClassicalEvaluator
# Tarrasch style
ConservativeEvaluator = RuleBasedEvaluator(
    generalRules=[
        createPstRules(piece={'P': 100, 'N': 300, 'B': 320,
                                        'R': 500, 'Q': 900, 'K': 60000})],
    gameStageRules={
        GameStage.Opening: (
            kingrules.mustBeAbleToCastle,
            kingrules.noEarlyKingMoves,
            kingrules.castleKingside(40),
            kingrules.castleQueenside,
            queenrules.noEarlyQueenAdvance
        )},
)

MorphyEvaluator = RuleBasedEvaluator(
    generalRules=[
        createPstRules(piece={'P': 100, 'N': 300, 'B': 310,
                                        'R': 500, 'Q': 900, 'K': 60000})],
    gameStageRules={
        GameStage.Opening: (
            kingrules.mustBeAbleToCastle,
            kingrules.noEarlyKingMoves,
            kingrules.castleKingside(40),
            kingrules.castleQueenside,
            developFast(110),
        )},
)
