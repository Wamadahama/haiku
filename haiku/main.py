import haiku
import syllables
import markovify
import generator

def main():

    # with open("res/corpus_texts/") as f:
    #      raw_text = f.read()

    haiku_generator = generator.Generator(corpus_directory='res/corpus_texts/')
    haiku.pretty_print(haiku_generator.generate_haiku())


def run_tests():
    results = syllables.compare_full_dictionary(data="string")
    print(results)

if __name__ == '__main__':
    main()
