from typing import List

from errors import NotEnoughPlayersError

from deck import Deck
from player import Player
from show_down import ShowDown

class Game:
    community_cards = []
    pot = [0]
    deck = None
    players = []
    active_players = []
    player_blind = {}

    def __init__(self, players: List[Player]):
        self.big_blind = 10
        self.small_blind = 5
        self.players = players
        self.active_players = self.players[:]
        self.deck = Deck()
        self.deck.shuffle_deck()
        if len(players) < 2:
            raise NotEnoughPlayersError("At least 2 players are required to start the game.")
        
        self.player_blind["Small"] = players[0]
        self.player_blind["Big"] = players[1]


    def deal_deck(self) -> None:
        for player in self.active_players:
            player.set_private_cards([self.deck.deck.pop(), self.deck.deck.pop()])

            if self.player_blind["Big"] == player:
                player.bet(self.big_blind, self.pot)
            if self.player_blind["Small"] == player:
                player.bet(self.small_blind, self.pot)


    def _trash_card(self) -> None:
        self.deck.deck.pop()

    def flop(self) -> None:
        self._trash_card()
        for _ in range(3):
            self.community_cards.append(self.deck.deck.pop())
    
    def turn(self) -> None:
        self._trash_card()
        self.community_cards.append(self.deck.deck.pop())
    
    def river(self) -> None:
        self._trash_card()
        self.community_cards.append(self.deck.deck.pop())
    
    def show_down(self):
        show_down = ShowDown(self.community_cards)

        player_score = {}
        for player in self.active_players:
            score = show_down.evaluate_hand(player.get_private_cards())
            player_score[player] = score
        
        max_score = 0
        max_player = None
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
    

    def reset_game(self) -> None:
        if len(self.active_players) == 1:
            raise Exception(f"Game over! Player {self.active_players[0].name} won!")

        self.deck = Deck()
        self.deck.shuffle_deck()
        self.deck.shuffle_deck()
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
        
