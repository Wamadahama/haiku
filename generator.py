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

    def generate_haiku(self, weight=10):
        """Generates a haiku based off of the text model, weight determines
        how many sources it will pull from"""
        sentences = [self.text_model.make_short_sentence(char_limit=35, tries=weight) for i in range(weight)]

        haiku = []

        for required_line_syll_count in self.HAIKU_FORMAT:
            generated_line = []
            # Pull a random sentence from the generated senteces
            sentence = sentences[random.randint(0, len(sentences)-1)]

            # Get a syllable count of the sentence
            words = sentence.split(" ")
            word_counts = [syllables.count_syllables(word) for word in words]

            current_syll_count = 0
            remaining_syllabes = (required_line_syll_count - current_syll_count)

            while True:
                # Determine how many syllables we have left
                options = [(word,count) for word,count in zip(words, word_counts)
                                            if count <= remaining_syllabes]

                # Get a random word from out options
                random_word_index = 0
                word_tuple = ()
                if len(options) == 0:
                    random_word_index = 0
                else:
                    random_word_index = random.randint(0, (len(options)-1))

                word_tuple = options[random_word_index]

                word = word_tuple[0]

                if word in generated_line:
                    next

                current_syll_count = word_tuple[1]

                remaining_syllabes -= current_syll_count
                generated_line.append(word)

                if remaining_syllabes <= 0:
                    break

                line_string = ' '.join(generated_line)

            haiku.append(line_string)

        return haiku
