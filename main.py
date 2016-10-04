import haiku
import urllib.request
import json
from bs4 import BeautifulSoup

def main():
    with open("Syllables.txt", encoding="cp1252") as syll_data:
        raw_file_text = syll_data.readline()
        print(raw_file_text.split("n·"))


if __name__ == '__main__':
    main()
