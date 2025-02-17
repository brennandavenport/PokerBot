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
        self.head = None
        self.active_player_count = 0

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
        
        
    def display(self) -> None:
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.active, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(Back to Head)")
    

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



    def update_big_blind(self, big_blind: PlayerNode) -> PlayerNode:
        if self.active_player_count == 1:
            raise EndOfGameError()

        if not self.head:
            return None
        
        temp = big_blind

        while True:
            if temp.data.is_active() and temp != big_blind:
                return temp
            
            temp = temp.next

    
    def update_small_blind(self, big_blind: PlayerNode) -> PlayerNode:
        if self.active_player_count == 1:
            raise EndOfGameError()

        if not self.head:
            return None
        
        temp = big_blind

        while True:
            if temp.active and temp != big_blind:
                return temp
            
            temp = temp.next


if __name__ == "__main__":
    table = Table()

    starting_amount = 1000

    print("Hello")

    player1 = Player('Bob', starting_amount, None)
    player2 = Player('Ben', starting_amount, None)
    player3 = Player('Alex', starting_amount, None)
    player4 = Player('James', starting_amount, None)
    player5 = Player('Richard', starting_amount, None)

    table.display()

    players = [player1, player2, player3, player4, player5]


    table.add_players(players)
    print("-------------------------------")

    big_blind = table.head
    small_blind = table.head.next

    print(big_blind.data.name)
    print(small_blind.data.name)

    table.display()

    big_blind = table.update_big_blind(big_blind)
    small_blind = table.update_small_blind(big_blind)

    print(big_blind.data.name)
    print(small_blind.data.name)

    table.display()

    table.update_active_players(player3)
    table.update_active_players(player4)
    table.update_active_players(player5)
    table.update_active_players(player1)
    try:
        big_blind = table.update_big_blind(big_blind)
        small_blind = table.update_small_blind(big_blind)
    except EndOfGameError:
        print("Game over")
        exit()

    print(big_blind.data.name)
    print(small_blind.data.name)

    table.display()