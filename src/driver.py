from game import Game
from player import Player
from strategies.random_strategy import RandomStrategy



def main():
    starting_amount = 1000
    testing_strategy = RandomStrategy('random')

    player1 = Player('Aditya', starting_amount, testing_strategy)
    player2 = Player('Raul', starting_amount, testing_strategy)
    player3 = Player('Alex', starting_amount, testing_strategy)
    player4 = Player('James', starting_amount, testing_strategy)
    player5 = Player('Arjun', starting_amount, testing_strategy)

    players = [player1, player2, player3, player4, player5]

    game = Game(players)
    for round_num in range(1):
        print("<------------New Round:", round_num, "--------------->")

        game.deal_deck()


        for player in players:
            print(player)

        #First round of betting
        # for player in game.active_players:

        game.print_pot()

        game.preflop()

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

        # Bugged method need to fix
        game.show_down()


        for player in players:
            print(player)
        

        game.reset_game()

        print("<---------------End of Round-------------->", end="\n\n")


if __name__ == "__main__":
    main()