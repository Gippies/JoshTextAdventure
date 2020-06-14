from joshtextadventure.input_manager import InputManager
from joshtextadventure.location import Location


class Game:
    def __init__(self):
        self.input_manager = InputManager()
        north_location = Location("You're on the edge of a cliff", None, None, None, None)
        self.test_location = Location('You are in a forrest', north_location, None, None, None)

    def run(self):
        while True:
            print(self.test_location)
            val = input("$: ")
            self.input_manager.parse_input(val)

