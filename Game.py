import os


class Game:

    def __init__(self, banner_text_file_string):
        self.list_of_players = []
        self.banner = banner_text_file_string

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




