from strategy import Strategy
from my_enum import Decision, GameStage

from typing import Tuple

class DeepLearningStrat(Strategy):
    def __init__(self, name):
        super().__init__(name)

    def handle_turn(self, private_cards, chips: int, community_cards, pot, game_stage, bet_to_call) -> Tuple[Decision, int]:
        pass