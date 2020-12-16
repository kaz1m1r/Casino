from Game import Game
from termcolor import colored

class RowOfSquares:
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


