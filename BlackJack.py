from Dealer import Dealer
from time import sleep
from Game import Game


class Blackjack(Game):

    def __init__(self, blackjack_banner):
        Game.__init__(self, blackjack_banner)
        self.welcome_message(blackjack_banner)

        self.dealer = Dealer()
        self.add_players()  # make player instances
        self.participants_two_cards()   # get every participant two cards
        self.play()

    def play(self):
        print(f"Dealer shows {self.dealer.hand[0].value} of {self.dealer.hand[0].suit}")
        print(f"Value is {self.value_first_card(self.dealer)}\n")
        self.player_hit()
        self.dealer_show_cards()
        for player in self.list_of_players:
            self.determine_winner(player, self.dealer)

    def dealer_show_cards(self):
        print("\nDealer has the following hand : ")
        for card in self.dealer.hand:
            print(f"{card.value} of {card.suit}")
        self.calculate_value_of_hand(self.dealer)
        if self.dealer.value_of_hand <= 16:
            print("\nDealer hits another card...\n")
            self.dealer.add_card_to_hand(self.dealer.get_upper_card_from_deck())
            sleep(2)
            print("His hand is now : ")
            for card in self.dealer.hand:
                print(f"{card.value} of {card.suit}")
            self.calculate_value_of_hand(self.dealer)
        print(f"\nValue of the dealer's hand is : {self.dealer.value_of_hand}")


    def player_hit(self):
        for player in self.list_of_players:
            print(f"Player {player.id} : {player.name} has :")
            self.calculate_value_of_hand(player)
            while True:
                for card in player.hand:
                    print(f"{card.value} of {card.suit}")
                print(f"Value of {player.name}'s hand is {player.value_of_hand}")
                if player.value_of_hand < 21:
                    choice = input("\nHit or pass?('h' or 'p') : ")
                    if choice == 'h':
                        player.add_card_to_hand(self.dealer.get_upper_card_from_deck())
                        print(f"Another card was dealt to {player.name}")
                        self.calculate_value_of_hand(player)
                    else:
                        print(f"Value of {player.name}'s hand : {player.value_of_hand}")
                        break
                else:
                    break


    def value_first_card(self, participant):
        """
        Calculate the value of the first card of a participant
        :param participant:
        :return: int
        """
        numerical_values = {"Jack": 10, "Queen": 10, "King": 10}
        value = 0
        if participant.hand[0].value == "Ace":
            value = 11
        elif participant.hand[0].value in numerical_values.keys():
            value = numerical_values[participant.hand[0].value]
        else:
            value = int(participant.hand[0].value)

        return value


    def calculate_value_of_hand(self, participant):
        """
        Calculate the value of the player/dealer's current hand
        """
        numerical_values = {"Jack": 10, "Queen": 10, "King": 10}
        if participant.value_of_hand == 0:  # no calculations performed regarding calculation the value of the player's hand
            for card in participant.hand:
                if card.value == "Ace":
                    if participant.value_of_hand + 11 <= 21:
                        participant.value_of_hand += 11
                    else:
                        participant.value_of_hand += 1
                elif card.value in numerical_values.keys():
                    participant.value_of_hand += numerical_values[card.value]
                else:
                    participant.value_of_hand += int(card.value)
        else: # calculation have been performed regarding the value of the player's hand
            if participant.hand[-1].value == "Ace":
                if participant.value_of_hand + 11 <= 21:
                    participant.value_of_hand += 11
                else:
                    participant.value_of_hand += 1
            elif participant.hand[-1].value in numerical_values.keys():
                participant.value_of_hand += numerical_values[participant.hand[-1].value]
            else:
                participant.value_of_hand += int(participant.hand[-1].value)

    def determine_winner(self, player, dealer):
        """
        Determines wether the player wins or loses from the dealer
        :param player:
        :param dealer:
        :return: None
        """
        if player.value_of_hand == 21 and len(player.hand) == 2:
            print(f"{player.name} was dealt a Black Jack so he wins!!")
        elif player.value_of_hand > 21 or (player.value_of_hand <= dealer.value_of_hand <= 21):
            print(f"Dealer wins from {player.name}!!!")
        else:
            print(f"{player.name} wins from the Dealer!!!")

    def participants_two_cards(self):
        """
        Every player and the dealer gets 2 cards from a shuffled deck
        """
        print("\n"
              "Dealing cards..."
              "\n")
        for _ in range(2):
            for player in self.list_of_players:
                player.add_card_to_hand(self.dealer.get_upper_card_from_deck())
            self.dealer.add_card_to_hand(self.dealer.get_upper_card_from_deck())

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
