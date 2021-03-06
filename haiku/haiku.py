import syllables
import helpers
import json

def parse_haiku(haiku_string, delim):
    """Parses a haiku where delim is the delimiter"""
    # Get a list of the lines
    lines = haiku_string.split(delim)

    # Separate the words on the lines
    separated_words = [[word.strip(".") for word in line.split(" ")] for line in lines]
    return separated_words

def get_haiku_syllables(parsed_haiku):
    """Returns a tuple  with the counts of syllables for each line"""
    line_counts = []

    for line in parsed_haiku:
        counter = 0
        for word in line:
            counter += syllables.count_syllables(word)
        line_counts.append(counter)

    return tuple(line_counts)

def pretty_print(haiku_list):
    for line in haiku_list:
        print(line)

def haiku_tests():
    """Tests all the known haikus in the haikus.json"""
    haiku_dict = helpers.read_json_file("res/haikus.json")

    for i,d in enumerate(haiku_dict):
        parsed_haiku = parse_haiku(d["haiku_string"], ",")
        print(get_haiku_syllables(parsed_haiku))
