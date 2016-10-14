import markovify
import syllables
import random

class Generator:

    def __init__(self, text, HAIKU_FORMAT=[5,7,5]):
        """Initialize the haiku generator """
        self.HAIKU_FORMAT = HAIKU_FORMAT
        self.text_model = markovify.Text(text)

    def update_model(self, text):
        """Updates the text model"""
        self.text_model = markovify.Text(text)

    def generate_haiku(self, weight=10):
        """Generates a haiku based off of the text model, weight determines
        how many sources it will pull from"""
        sentences = [self.text_model.make_sentence() for i in range(weight)]

        haiku = []

        for _,required_line_syll_count in self.HAIKU_FORMAT:
            # Pull a random sentence from the generated senteces
            sentence = sentences[random.randint(0, len(sentences))].trim()

            # Get a syllable count of the sentence
            words = sentence.split(" ")
            word_counts = [syllables.count_syllables(word) for word in words]

            # At first get a random word, this will be the base
            initial_word = words[random.randint(0, len(words))]
            initial_word_count = word_counts[words.index(initial_word)]

            # How many syllables do we have left after selecting an initial word
            remaining_syllabes = (initial_word_count - required_line_syll_count)

            if remaining_syllabes == 0:
                haiku.append(initial_word)
                continue

            # if we pulled a word to big right off the bat lets just restart
            if remaining_syllabes < 0:
                generate_haiku(self, weight)
            else:
            # lets grab some more words
                while True:
                    options = [(word,count) for word,count zip(words, word_counts)
                                                    if count < remaining_syllabes]
