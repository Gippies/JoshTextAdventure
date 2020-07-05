
class Parser:
    def __init__(self, game):
        self.game = game

    def parse_input(self, value):
        if value.upper() == 'N' or value.upper() == 'S' or value.upper() == 'E' or value.upper() == 'W':
            if self.game.player.current_location.locations[value.upper()] is not None:
                self.game.player.current_location = self.game.player.current_location.locations[value.upper()]
                self.game.printer.msg = str(self.game.player.current_location)
            else:
                self.game.printer.msg = "Invalid Location"
        elif value.lower() == 'exit':
            exit()
        else:
            self.game.printer.msg = "Invalid Command. Type 'help' for a list of commands."
