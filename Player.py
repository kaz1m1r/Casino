from Deck import Deck


class Player:

    def __init__(self, name, player_id):
        self.name = name
        self.id = id
        self.cards_of_player = []

    def add_card_to_hand(self, card):
        self.cards_of_player.append(card)