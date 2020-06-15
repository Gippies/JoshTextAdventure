from joshtextadventure.location import Location


class Game:
    def __init__(self):
        north_location = Location("You're on the edge of a cliff", {
            'N': None,
            'S': None,
            'E': None,
            'W': None
        })
        self.current_location = Location('You are in a forrest', {
            'N': north_location,
            'S': None,
            'E': None,
            'W': None
        })

    def run(self):
        while True:
            print(self.current_location)
            val = input("$: ")
            self.parse_input(val)

    def parse_input(self, value):
        if value.upper() == 'N' or value.upper() == 'S' or value.upper() == 'E' or value.upper() == 'W':
            if self.current_location.locations[value.upper()] is not None:
                self.current_location = self.current_location.locations[value.upper()]
            else:
                print("Invalid Location")
        if value.lower() == 'exit':
            exit()
