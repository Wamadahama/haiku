import urllib.request
from bs4 import BeautifulSoup

def convert_syllables_to_json
    with open("Syllables.txt", encoding="cp1252") as syll_data:
        raw_file_text = syll_data.read().split("\n")
        del(raw_file_text[-1])
        syllable_dictionary = [ {"word": line.split("=")[0], "count": get_count_from_line(line) } for line in raw_file_text]
        print(json.dumps(syllable_dictionary))

def get_count_from_line(line):
    syllable_line = line[line.index("=")+1:len(line)]
    return len(syllable_line.split("·"))

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
