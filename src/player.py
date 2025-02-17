from typing import List
from strategy import Strategy

from errors import AllInError

class Player:


    def __init__(self, name: str, starting_amount: int, strategy: Strategy):
        """Initialize a Player with a name, starting chips, and strategy."""


        # Set name
        self.name = name

        # Player chips
        self.chips = starting_amount

        # Player strategy
        self.strategy = strategy

        # Set activity of player
        self.round_active = True
        self.game_active = True

        # Initialize an empty list to store the player's private cards.
        self.private_cards = []

        
    # This function sets the players cards in each game
    def set_private_cards(self, cards: List[str]) -> None:
        self.round_active = True
        self.private_cards = cards


    # This function adds chips if the players wins a pot
    def add_chips(self, chips: int):
        self.chips += chips

    
    # This function determines if 
    def bet(self, bet_ammount: int, pot: List[int]) -> None:
        if bet_ammount > self.chips:
            pot[0] += self.chips
            self.chips = 0
            # Maybe add later if we need to know if a player is all in
            # raise AllInError()

        else:
            self.chips -= bet_ammount
            pot[0] += bet_ammount
        

    def is_balance_negative(self) -> bool:
        if self.chips <= 0:
            return True
        return False
    
    def fold(self) -> None:
        self.private_cards = []
        self.round_active = False

 
        
