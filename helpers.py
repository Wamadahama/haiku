import json
def read_json_file(filename):
    """Reads a json file and returns a python dictionary representation"""
    with open(filename) as json_file:
        return json.load(json_file)
