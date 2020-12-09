from Game import Game


class Roulette(Game):

    def __init__(self, roulette_banner):
        Game.__init__(self, roulette_banner)
        self.welcome_message(roulette_banner)
        self.add_players()