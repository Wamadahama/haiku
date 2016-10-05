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
        print(line)
        counter = 0
        for word in line:
            counter += syllables.count_syllables(word)
        line_counts.append(counter)

    return tuple(line_counts)

def scrape_haiku_poetry():
    """Scrapes http://www.haiku-poetry.org/famous-haiku.html and returns haikus as json"""
    haiku_website = "http://www.haiku-poetry.org/famous-haiku.html"
    raw_html = urllib.request.urlopen(haiku_website).read()

    soup = BeautifulSoup(raw_html, "html.parser")
    haiku_lists = soup.findAll("div", {"class": "col-right"})

    haikus = [[line.strip() for line in haiku.find_all('p')[1].get_text().split('\n')]
                            for haiku in haiku_lists]

    haikus = [",".join(haiku) for haiku in haikus]

    haiku_dict = []

    for i,haiku in enumerate(haikus):
        haiku_dict.append({ "id" : str(i), "haiku_string" : haiku })

    return json.dumps(haiku_dict)

def haiku_tests():
    haiku_dict = helpers.read_json_file("haikus.json")
    # with open("haikus.json") as json_file:
        # haiku_dict = json.load(json_file)

    for i,d in enumerate(haiku_dict):
        parsed_haiku = parse_haiku(d["haiku_string"], ",")
        print(get_haiku_syllables(parsed_haiku))
