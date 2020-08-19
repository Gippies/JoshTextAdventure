
class Location:
    locations = {}

    def __init__(self, location_dict):
        self.location_id = location_dict['id']
        Location.locations[location_dict['id']] = self
        self.description = location_dict['description']
        directions = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
        self.locations = {}
        for k, v in directions.items():
            self.locations[k] = Location.locations[location_dict[k]] if location_dict[k] is not None and location_dict[k] in Location.locations else None
            if location_dict[k] is not None:
                Location.locations[location_dict[k]].locations[v] = self

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
