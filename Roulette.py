from Game import Game
from MoneyErrors import TooLittleMoneyError
import random
import time


class Board:
    def __init__(self, landed_value):
        self.red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        self.black = [val for val in range(1, 37) if val not in self.red]
        self.left_column = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
        self.middle_column = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
        self.right_column = [num for num in range(1, 37) if num not in self.left_column and num not in self.middle_column]

        self.landed_value = landed_value
        self.landed_color = "red" if landed_value in self.red else "black"

class Roulette(Game):

    def __init__(self, roulette_banner, roulette_board):
        Game.__init__(self, roulette_banner, roulette_board)
        self.welcome_message()
        self.add_players()
        self.display_board()
        self.player_bets = {}
        for player in self.list_of_players:
            self.which_bets(player)

        self.rolled = self.roll_ball()
        print(f"\nBall landed on {self.rolled.landed_value} {self.rolled.landed_color}\n")
        time.sleep(1.5)
        for p in self.list_of_players:
            self.calculate_winnings(p, self.rolled)

    def calculate_winnings(self, player, board):
        """
        Calculating the winnings of a specific person. These winnings can be negative which
        indicates a loss of money
        :param board:
        :param player: Player object
        :return: None
        """
        winnings_dictionary_multiplier = {
            0: 2,
            1: 2,
            3: 2,
            4: 2,
            5: 2,
            6: 3,
            7: 3,
            8: 3
        }
        winnings = float(0)
        val = board.landed_value
        col = board.landed_color
        for bet in range(len(self.player_bets[player])):
            if bet == 0 and val in range(1, 19) \
                or bet == 1 and val in range(19, 37) \
                or bet == 2 and val % 2 == 0 \
                or bet == 3 and val % 2 == 1 \
                or bet == 4 and col == "black" \
                or bet == 5 and col == "red" \
                or bet == 6 and val in board.left_column \
                or bet == 7 and val in board.middle_column \
                or bet == 8 and val in board.right_column:

                winnings += float(winnings_dictionary_multiplier[bet]) * self.player_bets[player][bet]


        player.money += winnings
        print(f"Player {player.id} {player.name} won {winnings} dollars !!!")

    def roll_ball(self):
        """
        Rolling the roulette ball
        """
        landed_value = random.randrange(1, 37)
        print("Rolling ball...")
        time.sleep(3)
        return Board(landed_value)

    def which_bets(self, player):
        """
        Method that asks the specified player about the bets that he wants to make
        and stores the player's bets in a dictionary 'self.player_bets'
        :param player: Player
        :return: None
        """

        def betting_amount(question):
            while True:
                if player.money == float(0):
                    print("You got no money left so you cannot place any more bets")
                    print()
                    return None
                print(f"{player.money} dollars left")
                ask = input(question)
                try:
                    if player.money - float(ask) > float(0):
                        player.money -= float(ask)
                        return float(ask)
                    if player.money - float(ask) == float(0):
                        player.money -= float(ask)
                        return float(ask)
                    raise TooLittleMoneyError
                except ValueError:
                    print("Only type numbers e.g. '10.50'")
                except TooLittleMoneyError:
                    print("You got too little money to place that bet")
                    return None

        question = lambda subject : f"How much do you want to bet on {subject}? : "

        subjects = [
            "1-18 manque",
            "19-36 passe",
            "even",
            "odd",
            "black",
            "red",
            "left column",
            "middle column",
            "right column"
        ]

        bets = []

        print(f"Player {player.id} : {player.name}")
        print("----------\n")
        for subject in subjects:
            bet = betting_amount(question(subject))
            if bet == None:
                break
            bets.append(bet)

        # Adding a player object as a key to a dictionary and his bets as value
        self.player_bets[player] = bets


