class Player:
    def __init__(self, location):
        self.health = 10.0
        self.inventory = None
        self.current_location = location

    def __str__(self):
        player_str = 'Health: ' + str(self.health) + '\n'
        player_str += 'Inventory: ' + str(self.inventory) + '\n'
        player_str += str(self.current_location)
        return player_str
