from strategies.strategy import Strategy
from my_enum import Decision, GameStage

from typing import Tuple

import random

class RandomStrategy(Strategy):
    def __init__(self, name):
        super().__init__(name)

    def handle_turn(self, private_cards, chips: int, community_cards, pot, game_stage, bet_to_call) -> Tuple[Decision, int]:
        random_num = random.randint(1, chips)

        if bet_to_call > 0 and (chips - bet_to_call > 0):
            if random_num > bet_to_call:
                return (Decision.RAISE, random_num)
            else:
                return(Decision.CALL, bet_to_call)
        else:
            return(Decision.CHECK, 0)
            

    def receve_alert(self):
        pass



