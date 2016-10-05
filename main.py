import haiku
import syllables
import urllib.request
import json
import pprint
from bs4 import BeautifulSoup

def main():
    print(str(syllables.compare_to_dataset("test", 3)))

if __name__ == '__main__':
    main()
