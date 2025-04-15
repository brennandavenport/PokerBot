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
        # Game active
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


    def __iter__(self, start_node=None):
        """Iterator for the players at the table, starting from a given node.
        
        Yields only players whose `round_active` and `game_active` attributes are True.
        If `start_node` is provided, iteration begins from there; otherwise, it starts from `self.head`.
        """

        self.validate_player_count()

        # Assume start node is always in the list
        if start_node is None:
            start_node = self.head

        temp = start_node.next

        while temp is not start_node:
            if temp.data.round_active and temp.data.game_active:
                yield temp.data
            temp = temp.next


    def add_players(self, players: List[Player]) -> None:
        """
        Adds a list of players to a circular linked list.

        Args:
            players (List[Player]): A list of Player objects to be added.
        """
        for player in players:
            player_node = PlayerNode(player)  # Create a new node for the player
            self.active_player_count += 1  # Increment the active player count

            if not self.head:  
                # If the list is empty, set this node as the head and point it to itself (circular)
                self.head = player_node
                player_node.next = self.head
            else:
                # Traverse to the last node in the circular linked list
                temp = self.head
                while temp.next != self.head:  
                    temp = temp.next  

                # Insert the new node at the end and maintain the circular link
                temp.next = player_node
                player_node.next = self.head


    def deal_cards(self, deck) -> None:
        """
        Deals two private cards to each active player in a circular linked list.

        Args:
            deck: The deck object containing the cards to be dealt.
        """
        self.validate_player_count()  # Ensure there are enough players to play the game
        
        temp = self.head  # Start from the head of the circular linked list

        while True:
            if temp.data.game_active:  
                # If the player is active, give them two private cards from the deck
                temp.data.set_private_cards([deck.deck.pop(), deck.deck.pop()])

            temp = temp.next  # Move to the next player
            
            if temp == self.head:  
                # If we have completed one full cycle, stop
                break

        
    # Revisit if needed
    # def update_active_players(self, player: Player) -> None:
    #     #Linked list is empty
    #     if not self.head:
    #         return
        
    #     temp = self.head

    #     while True:
    #         if temp.data == player:
    #             temp.data.set_active(False)
    #             self.active_player_count -= 1
    #             return
            
    #         temp = temp.next

    #         # If we have looped back to the head, stop searching
    #         if temp == self.head:
    #             break


    def update_blind(self, blind: PlayerNode) -> PlayerNode:
        """
        Updates the blind position to the next active player.

        Args:
            blind (PlayerNode): The current blind position.

        Returns:
            PlayerNode: The next active player.
        """
        self.validate_player_count()
        
        temp = blind

        while True:
            temp = temp.next  # Move to the next player

            if temp.data.game_active and temp != blind:
                return temp


    def get_next_player(self, player: PlayerNode) -> PlayerNode:
        # Throw exception if head is empty and player count is == 1
        pass


    def validate_player_count(self) -> None:
        """
        Validates whether there are enough players to continue the game.

        Raises:
            Exception: If there are no players in the game.
            Exception: If there is only one or fewer active players.
        """
        if not self.head:
            # If the linked list is empty, no players exist
            raise Exception("There are no players")
        
        if self.active_player_count <= 1:
            # If there is only one or zero active players, the game cannot proceed
            raise Exception("There are not enough players")


if __name__ == "__main__":
    # Debug and test

    table = Table()

    starting_amount = 1000

    player1 = Player('Bob', starting_amount, None)
    player2 = Player('Ben', starting_amount, None)
    player3 = Player('Alex', starting_amount, None)
    player4 = Player('James', starting_amount, None)
    player5 = Player('Richard', starting_amount, None)

    players = [player1, player2, player3, player4, player5]


    table.add_players(players)

    big_blind = table.head.next
    small_blind = table.head

    # for _ in range(10):
    #     print("-------------------------------")
        
    #     print(f"Big blind: {big_blind.data}")
    #     print(f"Small blind: {small_blind.data}")

    #     print(table)

    #     small_blind = table.update_blind(small_blind)
    #     big_blind = table.update_blind(big_blind)
    
    for player in table:
        print(player)
        print(player.is_balance_negative())

    