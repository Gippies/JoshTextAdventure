from joshtextadventure.parser import Parser
from joshtextadventure.player import Player
from joshtextadventure.printer import Printer


class Game:
    def __init__(self):
        self.player = Player()
        welcome_msg = "Hello, welcome to Josh's Text Adventure!\n" + str(self.player)
        self.printer = Printer(welcome_msg)
        self.parser = Parser(self)

    def run(self):
        while True:
            self.printer.print_msg()
            val = input("$: ")
            self.parser.parse_input(val)
