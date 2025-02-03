from game import Game
from player import Player
import time

starting_amount = 1000
player1 = Player('Bob', starting_amount, None)
player2 = Player('Ben', starting_amount, None)
player3 = Player('Alex', starting_amount, None)
player4 = Player('James', starting_amount, None)
player5 = Player('Richard', starting_amount, None)

players = [player1, player2, player3, player4, player5]

game = Game(players)
for round_num in range(1000):
    print("<------------New Round:", round_num, "--------------->")

    game.deal_deck()


    for player in players:
        print("Player: ", player.name, ", hand: ", player.get_private_cards())

    #First round of betting
    # for player in game.active_players:

    game.print_pot()
    print("Small Blind: ", game.player_blind["Small"].name)
    print("Big Blind: ", game.player_blind["Big"].name)


    game.flop()
    game.print_community_cards()
    # time.sleep(1)

    #Second round of betting

    game.turn()
    game.print_community_cards()
    # time.sleep(1)

    #Third round of betting

    game.river()
    game.print_community_cards()
    # time.sleep(1)

    #Final round of betting

    game.show_down()


    for player in players:
        print("Player: ", player.name, ", pot: ", player.get_chips())
    

    game.reset_game()

    print("<---------------End of Round-------------->", end="\n\n")