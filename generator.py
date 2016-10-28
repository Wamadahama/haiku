import markovify
import syllables
import random
import threading

class Generator:

    def __init__(self, text, HAIKU_FORMAT=[5,7,5]):
        """Initialize the haiku generator """
        self.HAIKU_FORMAT = HAIKU_FORMAT
        self.text_model = markovify.Text(text)

    def update_model(self, text):
        """Updates the text model"""
        self.text_model = markovify.Text(text)

    def generate_haiku(self):
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
