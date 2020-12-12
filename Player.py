class Player:

    def __init__(self, name, player_id):
        self.name = name
        self.id = player_id
        self.hand = []
        self.money = float(1000)
        self.value_of_hand = 0

    def add_card_to_hand(self, card):
        self.hand.append(card)

    def show_hand(self):
        return self.hand