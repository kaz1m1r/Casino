from Game import Game
from termcolor import colored
import time
import os
import sys
import select


class Square:
    """
    Colored square class
    """

    def __init__(self, color_string):
        self.color = color_string

    def GetColor(self):
        return self.color

    def show(self):
        entire_square = "█"
        top_square = "▀"

        for _ in range(4):
            print(colored(10 * entire_square, self.color))

        print(colored(10 * top_square, self.color))


class Slotmachine(Game):

    def __init__(self, slotmachine_banner):

        Game.__init__(self, slotmachine_banner)
        self.welcome_message()
        self.add_players()

        self.colors_selected_squares = []
        self.square_colors = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
        self.play()

    def play(self):
        for _ in range(3):
            # no colors saved yet
            if len(self.colors_selected_squares) == 0:
                col1 = self.roll()
                self.colors_selected_squares.append(col1)

            # one color saved
            elif len(self.colors_selected_squares) == 1:
                col2 = self.roll(color1=self.colors_selected_squares[0])
                self.colors_selected_squares.append(col2)

            # two colors saved
            else:
                col3 = self.roll(color1=self.colors_selected_squares[0], color2=self.colors_selected_squares[1])
                self.colors_selected_squares.append(col3)

    def roll(self, color1=None, color2=None):
        """
        Simulating rolling
        :param color1: Color of the first (upper) square
        :param color2: Color of the second (middle) square
        :return: string (color)
        """
        # lambda for clearing screen
        clear_screen = lambda: os.system('cls' if os.name == 'nt' else 'clear')

        while True:
            for color in self.square_colors:

                # any key press will do but I say that one's ought to press enter
                print("Press Enter to stop!\n")

                if color1 is not None:
                    self.print_square(color1)

                if color2 is not None:
                    self.print_square(color2)

                self.print_square(color)
                time.sleep(0.5)

                # When key is pressed then color is returned
                if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                    clear_screen()
                    return color

                clear_screen()

    def print_square(self, color):
        """
        Method for printing a square of color 'color'
        :param color:
        :return: None
        """

        entire_square = "█"
        top_square = "▀"
        for _ in range(4):
            print(colored(10 * entire_square, color))

        print(colored(10 * top_square, color))
