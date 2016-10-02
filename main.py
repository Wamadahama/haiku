import syllables
import urllib.request
from bs4 import BeautifulSoup

def main():
    # parsed_haiku = parse_haiku("An old silent pond, A frog jumps into the pond, splash! Silence again", ",")
    # print(get_haiku_syllables(parsed_haiku))

    #<footer class="entry-footer clearfix">
    #<div class="col-right">
    # Second <div>
    haiku_website = "http://www.haiku-poetry.org/famous-haiku.html"
    raw_html = urllib.request.urlopen(haiku_website).read()

    soup = BeautifulSoup(raw_html, "html.parser")
    haiku_lists = soup.findAll("div", {"class": "col-right"})

    haikus = [[line.strip() for line in haiku.find_all('p')[1].get_text().split('\n')]
                            for haiku in haiku_lists]

    haikus = [",".join(haiku) for haiku in haikus]

    haiku_dict = []

    for i,haiku in enumerate(haikus):
        haiku_dict[i] = { "id" : str(i), "haiku_string" : haiku }

    print(haiku_dict)

if __name__ == '__main__':
    main()
