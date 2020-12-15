import os
from Player import Player

class Game:

    def __init__(self, banner_text_file_string, board_txt_file=None):
        self.list_of_players = []
        self.banner = "banners/"+banner_text_file_string
        if board_txt_file != None:
            self.board = "playing_boards/"+board_txt_file
        self.pot = 0  # sum of all bets from all players in this current round

    def display_board(self):
        """
        Display board nicely
        :param board_txt_file:
        :return: None
        """

        # making banner's absolute path using relative paths

        runtime_file_path = os.path.abspath(__file__)
        runtime_file_folder = os.path.dirname(runtime_file_path)
        banner_file_path = os.path.join(runtime_file_folder, self.board)
        print("\nBOARD THAT YOU'LL BE USING:\n")
        banner = open(banner_file_path, "r")
        for line in banner:
            print(line.strip("\n"))

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

    def welcome_message(self):
        """
        Nice welcome message
        :param banner_text_file:
        :return: None
        """

        # creating absolute path to 'banner_text_file' with relative paths

        runtime_file_path = os.path.abspath(__file__)
        print(runtime_file_path)
        runtime_file_folder = os.path.dirname(runtime_file_path)
        print(runtime_file_folder)
        banner_file_path = os.path.join(runtime_file_folder, self.banner)
        print(f"Banner path = {banner_file_path}")

        print("WELCOME TO:")
        banner = open(banner_file_path, "r")
        for line in banner:
            print(line.strip("\n"))
        print(30 * "~")




