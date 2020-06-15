
class Location:
    def __init__(self, description, locations):
        self.description = description
        self.locations = {'N': locations['N']}

        if locations['N'] is not None:
            locations['N'].locations['S'] = self

        self.locations['S'] = locations['S']
        if locations['S'] is not None:
            locations['S'].locations['N'] = self

        self.locations['E'] = locations['E']
        if locations['E'] is not None:
            locations['E'].locations['W'] = self

        self.locations['W'] = locations['W']
        if locations['W'] is not None:
            locations['W'].locations['E'] = self

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
