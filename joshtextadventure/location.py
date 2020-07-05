
class Location:
    def __init__(self, description, locations):
        self.description = description
        directions = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
        self.locations = {}
        for k, v in directions.items():
            self.locations[k] = locations[k]
            if locations[k] is not None:
                locations[k].locations[v] = self

    def __str__(self):
        travel_str = "You may travel: "
        if self.locations['N'] is not None:
            travel_str += "(N)orth "
        if self.locations['S'] is not None:
            travel_str += "(S)outh "
        if self.locations['E'] is not None:
            travel_str += "(E)ast "
        if self.locations['W'] is not None:
            travel_str += "(W)est"
        return self.description + '\n' + travel_str
