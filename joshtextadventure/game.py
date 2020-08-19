from joshtextadventure.json_loader import JSONLoader
from joshtextadventure.location import Location
from joshtextadventure.parser import Parser
from joshtextadventure.player import Player
from joshtextadventure.printer import Printer


class Game:
    def __init__(self):
        json_loader = JSONLoader('example.json')
        starting_location = None
        for location in json_loader.get_dict()['locations']:
            starting_location = Location(location)
        self.player = Player(starting_location)
        welcome_msg = "Hello, welcome to Josh's Text Adventure!\n" + str(self.player)
        self.printer = Printer(welcome_msg)
        self.parser = Parser(self)

    def run(self):
        while True:
            self.printer.print_msg()
            val = input("$: ")
            self.parser.parse_input(val)
