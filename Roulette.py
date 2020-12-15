from Game import Game
from MoneyErrors import TooLittleMoneyError
import random


class Board:
    def __init__(self, landed_value):
        self.value = landed_value
        self.landed_color = "red" if landed_value in self.red else "black"

        self.red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        self.black = [val for val in range(1, 37) if val not in self.red]
        self.left_column = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
        self.middle_column = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
        self.right_column = [num for num in range(1, 37) if num not in self.left_column and num not in self.middle_column]


class Roulette(Game):

    def __init__(self, roulette_banner, roulette_board):
        Game.__init__(self, roulette_banner, roulette_board)
        self.welcome_message()
        self.add_players()
        self.display_board()
        self.player_bets = {}
        self.which_bets(self.list_of_players[0])  # used to test self.which_bets(self,player) method
        self.rolled = self.roll_ball()
        self.calculate_winnings(self.list_of_players[0])

    def calculate_winnings(self, player, board):
        """
        Calculating the winnings of a specific person. These winnings can be negative which
        indicates a loss of money
        :param landed_value: Landed value object
        :param player: Player object
        :return: float
        """
        winnings_dictionary_multiplier = {0: 2, 1: 2, 3: 2, 4: 2, 5: 2, 6: 3, 7: 3, 8: 3}
        potential_winning = 0
        for bet in range(len(self.player_bets[player])):
            potential_winning += self.player_bets[player][bet] * winnings_dictionary_multiplier[bet]
        return potential_winning

    def roll_ball(self):
        """
        Rolling the roulette ball
        """
        landed_value = random.randrange(1, 37)
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
            "19-25 passe",
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

        self.player_bets[player] = bets


