import haiku
import syllables
import markovify
import generator

def main():
    with open("res/corpus_texts/alice.txt") as f:
         raw_text = f.read()

    haiku_generator = generator.Generator(raw_text, [5,7,5])

    haiku.pretty_print(haiku_generator.generate_haiku(weight=1000))


def run_tests():
    results = syllables.compare_full_dictionary(data="string")
    print(results)

if __name__ == '__main__':
    main()
