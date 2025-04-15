from my_enum import FoldStatus, AllIn


class Pot:
    def __init__(self, players):
        # Pot size
        self.main_pot = 0
        # How much each player has bet in a round
        self.players_bets = {player : 0 for player in players}
        # How many chips each players has left
        self.player_chips = {player : player.get_chips for player in players}
        # Who has folded
        self.player_fold = {player : FoldStatus.FALSE for player in players}
        # Who is all in
        self.player_all_in = {player : AllIn.FALSE for player in players}



    

