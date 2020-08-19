import json


class JSONLoader:
    def __init__(self, fn):
        self.filename = fn

    def get_dict(self):
        with open(self.filename) as f:
            data = json.load(f)
        return data
