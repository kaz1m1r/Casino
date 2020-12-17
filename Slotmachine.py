from Game import Game
from termcolor import colored
import time


class Square:
    """
    Colored square class
    """

    def __init__(self, color_string):
        self.color = color_string

    def show(self):
        entire_square = "█"
        top_square = "▀"

        for _ in range(4):
            print(colored(10 * entire_square, self.color))
            print(colored(10 * entire_square, self.color))
            print(colored(10 * entire_square, self.color))
            print(colored(10 * entire_square, self.color))
            print(colored(10 * top_square, self.color))


class Slotmachine(Game):

    def __init__(self, slotmachine_banner):

        Game.__init__(self, slotmachine_banner)
        self.welcome_message()
        self.add_players()

        self.selected_squares = []
        self.square_colors = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
        self.roll()

    def roll(self):
        """
        Simulating rolling
        :return: None
        """

        while True:
            for color in self.square_colors:
                self.print_square(color)
                time.sleep(0.05)

    def print_square(self, color):
        """
        Method for printing a square of color 'color'
        :param color:
        :return: None
        """

        entire_square = "█"
        top_square = "▀"

        print(colored(10 * entire_square, color))
        print(colored(10 * entire_square, color))
        print(colored(10 * entire_square, color))
        print(colored(10 * entire_square, color))
        print(colored(10 * top_square, color))
