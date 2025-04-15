from typing import List
from strategies.strategy import Strategy
from my_enum import Decision, GameStage, FoldStatus, AllIn
from pot import Pot

from errors import InvaildValueError

# Decide what turn it is based on community cards
GAMESTAGE_MAP = {0: GameStage.PREFLOP, 3: GameStage.FLOP, 4: GameStage.TURN, 5: GameStage.RIVER}

class Player:
    # Initialize a Player with a name, starting chips, and strategy.
    def __init__(self, name: str, starting_amount: int, strategy: Strategy):
        # Set name
        self.name = name

        # Player chips
        self.chips = starting_amount

        # Amout a player has bet in a given round
        self.round_bets = 0

        # Player strategy
        self.strategy = strategy

        # Set activity of player
        self.round_active = True
        self.game_active = True

        # Initialize an empty list to store the player's private cards.
        self.private_cards = []

        # All in tracker
        self.all_in = False

    def __str__(self):
        return f"Name: {self.name} | Chips: {self.chips} | Strategy: {self.strategy} | Private cards: {self.private_cards}"

    
    def turn(self, community_cards, pot):
        game_stage = GAMESTAGE_MAP.get(len(community_cards), None)

        # print(game_stage)
        # print(f"Len of community cards: {len(community_cards)}, community cards: {community_cards}")
        if game_stage is None:
            raise InvaildValueError
        
        decision, amount = self.strategy.handle_turn(self.private_cards, self.chips, community_cards, pot, game_stage, 0)

        if decision == Decision.CHECK:
            return

        elif decision == Decision.FOLD:
            self.fold(pot)
            return

        # Otherwise bet the amount into pot regardless of call or raise
        self.bet(amount, pot)
            

    # This function sets the players cards in each game
    def set_private_cards(self, cards: List[str]) -> None:
        self.round_active = True
        self.private_cards = cards


    # This function adds chips if the players wins a pot
    def add_chips(self, chips: int):
        self.chips += chips
        self.round_bets = 0

    def get_chips(self):
        return self.chips

    
    # This function bets the players chips with no saftey checks
    def bet(self, bet_ammount: int, pot: Pot) -> None:
        if self.all_in:
            return
        if bet_ammount > self.chips:
            # Update general pot
            pot.main_pot += self.chips

            # Update individual bets made by player
            pot.players_bets[self] += self.chips
            pot.player_chips[self] = 0
            pot.player_all_in[self] = AllIn.TRUE

            # Set all_in flag, set player chips to 0
            self.chips = 0
            self.all_in = True
        else:
            # Update individual bets made by player
            pot.players_bets[self] += bet_ammount

            # Update players personal chips remaining
            self.chips -= bet_ammount

            # Update general pot
            pot.main_pot += bet_ammount


    # Prob depricated - remove later
    def is_balance_negative(self) -> bool:
        return True if self.chips <= 0 else False
    

    def fold(self, pot) -> None:
        pot.player_fold[self] = FoldStatus.TRUE
        self.private_cards = []
        self.round_active = False
        self.round_bets = 0

 
        
