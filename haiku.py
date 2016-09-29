import syllables

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

    print(parsed_haiku)

    for line in parsed_haiku:
        counter = 0
        for word in line:
            counter += syllables.count_syllables(word)
            print(counter)
        line_counts.append(counter)

    return tuple(line_counts)



def main():
    print(syllables.count_syllables("A"))
    print(syllables.count_syllables("frog"))
    print(syllables.count_syllables("jumps"))
    print(syllables.count_syllables("into"))
    print(syllables.count_syllables("the"))
    print(syllables.count_syllables("pond"))

    parsed_haiku = parse_haiku("An old silent pond, A frog jumps into the pond, splash! Silence again", ",")
    print(get_haiku_syllables(parsed_haiku))

if __name__ == '__main__':
    main()
