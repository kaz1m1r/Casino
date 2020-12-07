from Card import Card


class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in ["Hearts", "Clovers", "Diamonds", "Spades"]:
            for value in [str(value) for value in range(2, 11)] + ["Jack", "Queen", "King", "Acd"]:
                self.all_cards.append(Card(value, suit))