import haiku
import syllables
import markovify


def main():
    #
    # text_model = markovify.Text(text)
    #
    # for i in range(5):
    #     print(text_model.make_sentence())
    #
    run_tests()

def run_tests():
    results = syllables.compare_full_dictionary(data="string")
    print(results)

if __name__ == '__main__':
    main()
