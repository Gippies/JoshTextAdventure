
class Parser:
    def parse_input(self, value, printer, player):
        if value.upper() == 'N' or value.upper() == 'S' or value.upper() == 'E' or value.upper() == 'W':
            if player.current_location.locations[value.upper()] is not None:
                player.current_location = player.current_location.locations[value.upper()]
                printer.msg = str(player.current_location)
            else:
                printer.msg = "Invalid Location"
        elif value.lower() == 'exit':
            exit()
        else:
            printer.msg = "Invalid Command. Type 'help' for a list of commands."
