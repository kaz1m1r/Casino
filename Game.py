import os
from Player import Player

class Game:

    def __init__(self, banner_text_file_string):
        self.list_of_players = []
        self.banner = banner_text_file_string

    def add_players(self):
        """
        Create list taf player objects
        :return: None
        """
        while True:
            try:
                amount_of_players = int(input("Enter amount of players : "))
                break
            except ValueError:
                print("Enter an integer (whole number such as 2, 3 etc) : ")
        list_of_names = []
        for player in range(amount_of_players):
            list_of_names.append(input(f"Name of Player {player + 1} : "))
        for name in range(len(list_of_names)):
            self.list_of_players.append(Player(list_of_names[name], name + 1))

    def welcome_message(self, banner_text_file):
        """
        Nice welcome message
        :param banner_text_file:
        :return: None
        """

        # creating absolute path to 'banner_text_file' with relative paths

        runtime_file_path = os.path.abspath(__file__)
        runtime_file_folder = os.path.dirname(runtime_file_path)
        banner_file_path = os.path.join(runtime_file_folder, banner_text_file)

        print("WELCOME TO:")
        banner = open(banner_file_path, "r")
        for line in banner:
            print(line.strip("\n"))
        print(30 * "~")




