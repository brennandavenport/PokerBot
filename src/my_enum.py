from enum import Enum

class Decision(Enum):
    CHECK = 'check'
    FOLD = 'fold'
    CALL = 'call'
    RAISE = 'raise'

class GameStage(Enum):
    PREFLOP = 'preflop'
    FLOP = 'flop'
    TURN = 'turn'
    RIVER = 'river'

class FoldStatus(Enum):
    TRUE = True
    FALSE = False

class AllIn(Enum):
    TRUE = True
    FALSE = False