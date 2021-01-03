from rule_based_eval import RuleBasedEvaluator, GameStage
from pst_rules import createPstRules
import playsharp_rules
import kingrules
import queenrules

# ClassicalEvaluator
# Tarrasch style
ConservativeEvaluator = RuleBasedEvaluator(
    name="Classical:Tarrasch",
    generalRules=[
        createPstRules(piece={'P': 100, 'N': 300, 'B': 320,
                                        'R': 500, 'Q': 900, 'K': 60000})],
    gameStageRules={
        GameStage.Opening: (
            kingrules.unableToCastle(-200),
            kingrules.earlyKingMoves(-100),
            kingrules.castleKingside(40),
            kingrules.castleQueenside(30),
            queenrules.earlyQueenAdvance(-50)
        ),
        GameStage.Middlegame: (),
        GameStage.Endgame: ()
    },

)

MorphyEvaluator = RuleBasedEvaluator(
    name="Romantic:Morphy",
    generalRules=[
        createPstRules(piece={'P': 100, 'N': 300, 'B': 310,
                                        'R': 500, 'Q': 900, 'K': 60000})],
    gameStageRules={
        GameStage.Opening: (
            kingrules.unableToCastle(-200),
            kingrules.earlyKingMoves(-300),
            kingrules.castleKingside(50),
            kingrules.castleQueenside(20),
            queenrules.earlyQueenAdvance(10),
            playsharp_rules.developFast(60),
            playsharp_rules.occupyCenter(40),
        ),
        GameStage.Middlegame: (),
        GameStage.Endgame: ()},
)
