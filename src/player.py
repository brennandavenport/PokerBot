from typing import List
from strategy import Strategy

class Player:
    _private_cards = []
    _chips = 0
    _strategy = None
    

    def __init__(self, name: str, starting_amount: int, strategy: Strategy):
        self.name = name
        self._chips = starting_amount
        self._strategy = strategy

    def is_active(self) -> bool:
        return self.active
    
    def set_private_cards(self, cards: List[str]) -> None:
        self.active = True
        self._private_cards = cards

    def get_private_cards(self) -> List[str]:
        return self._private_cards
    
    def bet(self, bet_ammount: int, pot: List[int]) -> None:
        if bet_ammount > self._chips:
            pot[0] += self._chips
            self._chips = 0

        else:
            self._chips -= bet_ammount
            pot[0] += bet_ammount
        

    def is_balance_negative(self) -> bool:
        if self._chips <= 0:
            return True
        return False
    
    def fold(self) -> None:
        self._private_cards = []
        self.active = False

    def add_chips(self, chips: int):
        self._chips += chips
        
    def get_chips(self):
        return self._chips
