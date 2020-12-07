from random import randrange
from Deck import Deck


class Dealer:

    def __init__(self):
        self.deck = Deck()
        self.shuffle_deck()
        self.hand = []
        self.value_of_hand = 0

    def get_hand(self):
        return self.hand

    def get_first_card_from_hand(self):
        print(f"{self.hand[0].value} of {self.hand[0].suit}")

    def add_card_to_hand(self, card):
        self.hand.append(card)

    def get_upper_card_from_deck(self):
        card = self.deck.all_cards[-1]
        self.deck.all_cards.pop(len(self.deck.all_cards) - 1)
        return card

    def shuffle_deck(self):
        for times_shuffled in range(1000):
            first_index = randrange(5, 20)
            first_subset = self.deck.all_cards[:first_index]
            second_index = randrange(32)
            second_subset = self.deck.all_cards[first_index: first_index + second_index]
            third_subset = self.deck.all_cards[first_index + second_index:]
            self.deck.all_cards = first_subset + third_subset + second_subset
