import markovify
import syllables
import random
import threading
from glob import glob

class Generator:

    def __init__(self, text='', HAIKU_FORMAT=[5,7,5], corpus_directory=''):
        """Initialize the haiku generator """
        self.HAIKU_FORMAT = HAIKU_FORMAT

        # IF they ppassed in the directory then
        # we want to get all of the files and
        # combine the markov chains
        if corpus_directory != '':
            files = glob(corpus_directory + "*")
            chains = []

            # Create a list of chains by reading the files
            for file in files:
                with open(file, encoding="utf-8") as f:
                    raw_text = f.read()
                chains.append(markovify.Text(raw_text))

            # Combine the chains
            self.text_model = markovify.combine(chains)

        else:
            # Else just use the passed text
            self.text_model = markovify.Text(text)

    def update_model(self, text):
        """Updates the text model"""
        self.text_model = markovify.Text(text)

    def generate_haiku(self):
        """Generates a haiku based on the markov chain that is assigned to the class"""
        haiku = []
        for required_line_syll_count in self.HAIKU_FORMAT:
            while True:
                sentence = self.text_model.make_short_sentence(char_limit=120)

                if sentence is None:
                    continue

                words = sentence.split(" ")
                word_counts = [syllables.count_syllables(word) for word in words]

                if sum(word_counts) == required_line_syll_count:
                    haiku.append((" ".join(words)).strip("."))
                    break

        return haiku
