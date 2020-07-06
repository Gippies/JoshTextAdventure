
class Parser:
    commands = {
        'N': 'Travel North',
        'S': 'Travel South',
        'E': 'Travel East',
        'W': 'Travel West',
        'help': 'Display this message',
        'exit': 'Quits the game'
    }

    def __init__(self, game):
        self.game = game

    def parse_input(self, value):
        value = value.strip().lower()
        if value == 'n' or value == 's' or value == 'e' or value == 'w':
            if self.game.player.current_location.locations[value.upper()] is not None:
                self.game.player.current_location = self.game.player.current_location.locations[value.upper()]
                self.game.printer.msg = str(self.game.player.current_location)
            else:
                self.game.printer.msg = "Invalid Location"
        elif value == 'help':
            msg = ''
            for k, v in Parser.commands.items():
                msg += '"' + k + '": ' + v + '\n'
            self.game.printer.msg = msg
        elif value == 'exit':
            exit()
        else:
            self.game.printer.msg = "Invalid Command. Type 'help' for a list of commands."
