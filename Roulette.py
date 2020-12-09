from Player import Player
from Deck import Deck
import os


class Roulette:

    def __init__(self):
        self.welcome_message()

    def welcome_message(self):
        """
        print nice welcome message to roulette
        :return: None
        """

        # constructing new absolute path based on relative paths

        absFilePath = os.path.abspath(__file__)
        parentDir = os.path.dirname(absFilePath)
        roulette_banner_path = os.path.join(parentDir, "roulette_banner.txt")
        roulette_banner = open(roulette_banner_path, "r")

        print("WELCOME TO \n")
        for line in roulette_banner:
            print(line.strip("\n"))
        roulette_banner.close()

        print("\n"
              "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
              "\n")