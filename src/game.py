from typing import List

from errors import NotEnoughPlayersError

from deck import Deck
from table import Table
from player import Player
from show_down import ShowDown
from pot import Pot

class Game:
    def __init__(self, players: List[Player]):
        #Min requirments to start game
        if len(players) < 2:
            raise NotEnoughPlayersError("At least 2 players are required to start the game.")

        # Init game const
        self.community_cards = []
        self.big_blind_amount = 10
        self.small_blind_amount = 5 

        # Init pot with player info, chips, has_folded?
        self.pot = Pot(players)

        # Init table
        self.table = Table()
        self.table.add_players(players)

        # Init deck
        self.deck = Deck()
        self.deck.shuffle_deck()

        # Init blinds
        self.small_blind_ptr = self.table.head
        self.big_blind_ptr = self.table.head.next

        

    def deal_deck(self) -> None:
        """
        Deals the cards to start the game
        - Sets big blind and small blind
        """
        # Deal cards to players at table
        self.table.deal_cards(self.deck)

        # Update pot with blinds - deal with all in on blind later
        self.small_blind_ptr.data.bet(self.small_blind_amount, self.pot)
        self.big_blind_ptr.data.bet(self.big_blind_amount, self.pot)

        
    def betting_round(self) -> None:
        # Find player after big blind assume he exists
        start_player_ptr = self.big_blind_ptr.next

        # Check for self reference
        if start_player_ptr == self.big_blind_ptr:
            raise Exception("Player after big blind equals big blind?")
        
        # Start_player_ptr is now the player whos turn it is to start the betting
        
        for player in self.table.__iter__(start_player_ptr):
            player.turn(self.community_cards, self.pot)
        
        
           

    def preflop(self) -> None:
        self.betting_round()

    def _trash_card(self) -> None:
        self.deck.deck.pop()

    def flop(self) -> None:
        self._trash_card()
        for _ in range(3):
            self.community_cards.append(self.deck.deck.pop())
        self.betting_round()
    
    def turn(self) -> None:
        self._trash_card()
        self.community_cards.append(self.deck.deck.pop())
        self.betting_round()
    
    def river(self) -> None:
        self._trash_card()
        self.community_cards.append(self.deck.deck.pop())
        self.betting_round()
    
    # To-do refactor
    def show_down(self):
        show_down = ShowDown(self.community_cards)

        

        player_score = {}
        for player in self.table:
            score = show_down.evaluate_hand(player.get_private_cards())
            player_score[player] = score
        
        max_score, max_player = 0, None
    
        for player in player_score:
            if max_score < player_score[player]:
                max_score = player_score[player]
                max_player = player

            print("Player: ", player.name, ", score: ", player_score[player])

        self.payout(max_player)
        
        for player in self.active_players:
            if player == max_player:
                continue

            if player.is_balance_negative():
                self.active_players.remove(player)
    

    # To-do refactor
    def reset_game(self) -> None:
        # if len(self.active_players) == 1:
        #     raise Exception(f"Game over! Player {self.active_players[0].name} won!")
        
        self.deck = Deck()
        self.deck.shuffle_deck()

        player0 = self.player_blind["Small"]  # Previous Small Blind
        
        # Step 1: Find the next active player for Small Blind
        try:
            index_player0 = self.active_players.index(player0)  # Get index in active players
        except ValueError:
            # If player0 is not in active_players, find the next available active player in self.players
            index_player0 = self.players.index(player0)
            sb_new_round = (index_player0 + 1) % len(self.players)
            
            while self.players[sb_new_round] not in self.active_players:
                sb_new_round = (sb_new_round + 1) % len(self.players)

            index_player0 = self.active_players.index(self.players[sb_new_round])  # Update index in active players

        # Step 2: Assign Small Blind and Big Blind to next available players
        sb_index = (index_player0 + 1) % len(self.active_players)
        bb_index = (index_player0 + 2) % len(self.active_players)

        self.player_blind["Small"] = self.active_players[sb_index]
        self.player_blind["Big"] = self.active_players[bb_index]

        # Step 3: Reset pot and community cards
        self.pot = [0]  # Store pot in a list for pass-by-reference behavior
        self.community_cards = []


    def print_community_cards(self) -> None:
        print(self.community_cards)
    

    def print_pot(self) -> None:
        print(self.pot)


    def payout(self, winner: Player):
        winner.add_chips(self.pot[0])
        
