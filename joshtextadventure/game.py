from joshtextadventure.parser import Parser
from joshtextadventure.player import Player
from joshtextadventure.printer import Printer


class Game:
    def __init__(self):
        self.player = Player()
        self.printer = Printer(self.player)
        self.parser = Parser()

    def run(self):
        while True:
            self.printer.print_msg()
            val = input("$: ")
            self.parser.parse_input(val, self.printer, self.player)
