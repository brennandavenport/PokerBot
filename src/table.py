from errors import EndOfGameError

from typing import List
from player import Player

# Node class for circlular linked list
class PlayerNode:
    def __init__(self, player: Player):
        self.data = player
        self.next = None

# Circular linked list that stores the player info
class Table:
    def __init__(self):
        """Initializes a Table object, setting the head to None and active player count to 0."""
        self.head = None
        self.active_player_count = 0


    def __str__(self):
        """
        Returns a string representation of the table's current players and their statuses.
        
        If the table has no players, returns a message indicating that. Otherwise, 
        iterates through all players and returns their name, and whether they are active
        in the game or round.
        
        Returns:
            str: A string with details about each player in the game.
        """
        # If there are no players at the table, return a message
        if not self.head:
            return "Table has no players"
        
        player_string = ""
        temp = self.head  # Start from the first player
        while True:
            # Concatenate player details to the string
            player_string += f"Player Name: {temp.data.name}, game active: {temp.data.game_active}, round active: {temp.data.round_active}\n"
            temp = temp.next  # Move to the next player
            if temp == self.head:  # Break the loop when we return to the head
                break
        
        return player_string


    def __len__(self):
        """Returns the number of active players at the table."""
        return self.active_player_count



    def add_players(self, players: List[Player]) -> None:
        for player in players:
            player_node = PlayerNode(player)
            self.active_player_count += 1

            if not self.head:
                self.head = player_node
                player_node.next = self.head
            else:
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next

                temp.next = player_node
                player_node.next = self.head


    def deal_cards(self, deck) -> None:
        if not self.head:
            return
        
        temp = self.head

        while True:
            if temp.data.game_active:
                temp.data.set_private_cards([deck.deck.pop(), deck.deck.pop()])

            temp = temp.next
        
            if temp == self.head:
                break
        
        

    def update_active_players(self, player: Player) -> None:
        #Linked list is empty
        if not self.head:
            return
        
        temp = self.head

        while True:
            if temp.data == player:
                temp.data.set_active(False)
                self.active_player_count -= 1
                return
            
            temp = temp.next

            # If we have looped back to the head, stop searching
            if temp == self.head:
                break


    # Need to be fixed
    def update_big_blind(self, big_blind: PlayerNode) -> PlayerNode:
        self.validate_player_count(player=big_blind)
        
        temp = big_blind

        while True:
            if temp.data.is_active() and temp != big_blind:
                return temp
            
            temp = temp.next

    # NEed to be fixed
    def update_small_blind(self, small_blind: PlayerNode) -> PlayerNode:
        self.validate_player_count(player=small_blind)
        
        temp = small_blind

        while True:
            if temp.active and temp != small_blind:
                return temp
            
            temp = temp.next

    def get_next_player(self, player: PlayerNode) -> PlayerNode:
        # Throw exception if head is empty and player count is == 1
        pass

    # IF there is an error then thrwo it
    def validate_player_count(self, player: PlayerNode) -> None:
        if not self.head:
            raise Exception("There are no players")
        
        if self.active_player_count <= 1:
            raise Exception("There are not enought players")

if __name__ == "__main__":
    table = Table()

    starting_amount = 1000

    print("Hello")

    player1 = Player('Bob', starting_amount, None)
    player2 = Player('Ben', starting_amount, None)
    player3 = Player('Alex', starting_amount, None)
    player4 = Player('James', starting_amount, None)
    player5 = Player('Richard', starting_amount, None)

    print(table)

    players = [player1, player2, player3, player4, player5]


    table.add_players(players)
    print("-------------------------------")

    big_blind = table.head
    small_blind = table.head.next

    print(big_blind.data.name)
    print(small_blind.data.name)

    print(table)

    big_blind = table.update_big_blind(big_blind)
    small_blind = table.update_small_blind(big_blind)

    print(big_blind.data.name)
    print(small_blind.data.name)

    print(table)

