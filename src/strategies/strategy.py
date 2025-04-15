from my_enum import Decision

from typing import Tuple

class Strategy:
    def __init__(self, name=None):
        self.name = name if name is not None else "No name given"

    def __str__(self):
        return f"Strategy name: {self.name}"

    def handle_turn(self, private_cards, chips: int, community_cards, pot, game_stage, bet_to_call) -> Tuple[Decision, int]:
        # Children will implement specific strategy logic here
        # Place holder example
        # Have Traders Members implement the strategies
        return (Decision.FOLD, 0)
    


