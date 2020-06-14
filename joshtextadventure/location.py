
class Location:
    def __init__(self, description, north_location, south_location, east_location, west_location):
        self.description = description

        self.north_location = north_location
        if north_location is not None:
            north_location.south_location = self

        self.south_location = south_location
        if south_location is not None:
            south_location.north_location = self

        self.east_location = east_location
        if east_location is not None:
            east_location.west_location = self

        self.west_location = west_location
        if west_location is not None:
            west_location.east_location = self

    def __str__(self):
        travel_str = "You may travel: "
        if self.north_location is not None:
            travel_str += "(N)orth "
        if self.south_location is not None:
            travel_str += "(S)outh "
        if self.east_location is not None:
            travel_str += "(E)ast "
        if self.west_location is not None:
            travel_str += "(W)est"
        return self.description + '\n' + travel_str
