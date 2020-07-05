from joshtextadventure.location import Location


class Player:
    def __init__(self):
        self.health = 10.0
        self.inventory = None
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

    def __str__(self):
        player_str = 'Health: ' + str(self.health) + '\n'
        player_str += 'Inventory: ' + str(self.inventory) + '\n'
        player_str += str(self.current_location)
        return player_str
