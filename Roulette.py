from Game import Game


class Roulette(Game):

    def __init__(self, roulette_banner, roulette_board):
        Game.__init__(self, roulette_banner)
        self.welcome_message(roulette_banner)
        self.add_players()
        self.display_board(roulette_board)
        self.player_bets = {}

        self.which_bets(self.list_of_players[0])

    def which_bets(self, player):
        """
        Method that asks the specified player about the bets that he wants to make
        and stores the player's bets in a dictionary 'self.player_bets'
        :param player: Player
        :return: None
        """

        def betting_amount(question):
            while True:
                print(f"{player.money} dollars left")
                ask = input(question)
                try:
                    if player.money - float(ask) >= 0:
                        player.money -= float(ask)
                        return float(ask)
                    raise Exception
                except ValueError:
                    print("Only type numbers e.g. '10.50'")
                except Exception:
                    print("You got too little money")

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
        print("--------------\n")
        for subject in subjects:
            bets.append(betting_amount(question(subject)))

        self.player_bets[player] = bets


