from random import randrange
from Deck import Deck


class Dealer:

    def __init__(self):
        self.deck = Deck()
        self.shuffle_deck()
        self.cards_of_dealer = []

    def add_card_to_hand(self, card):
        self.cards_of_dealer.append(card)

    def get_upper_card(self):
        card = self.deck.all_cards[-1]
        self.deck.all_cards.pop(card)
        return card

    def shuffle_deck(self):
        for times_shuffled in range(1000):
            first_index = randrange(5, 20)
            first_subset = self.deck.all_cards[:first_index]
            second_index = randrange(32)
            second_subset = self.deck.all_cards[first_index: first_index + second_index]
            third_subset = self.deck.all_cards[first_index + second_index:]
            self.deck.all_cards = first_subset + third_subset + second_subset
