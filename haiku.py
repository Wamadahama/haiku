
def is_vowel?(charcater):
    """Determines whether a character is a vowel or not """
    vowels = ["A", "E", "I", "O", "U"]
    if character is in vowels:
        return True
    else:
        return False

def count_vowels(search_string):
    """Counts the vowels in a string """
    count = 0
    for character in search_string:
        if is_vowel?(character):
            count += 1
    return count

def has_contiguous_vowels(search_string):
    """ Determines if there is contiguous vowels in a search string and if there is then search it"""
    last_char_vowel = False
    contiguous = False
    locations = []
    for character,counter in enumerate(search_string):

        if last_char_vowel and is_vowel?(character):
            contiguous = True
            locations.push((counter-1, counter))
            last_char_vowel = False

        if is_vowel?(character):
            last_char_vowel = True

    return {"contiguous?": contiguous, "locations": locations}

def trim_contiguous_vowels(search_string, locations):
    """Remove one of the contiguous values"""
    "".join([char for c,i in enumerate(search_string) if i not in locations[1])


def count_syllables(input_string):
    syllable_count = 0

    # Check if there are contiguous vowels in the statement
    results = has_contiguous_vowels(input_string)

    # If there are contiguous values we can remove them and then count the vowels
    if results["contiguous?"]:
        input_string = trim_contiguous_vowels(input_string, results["locations"])
        syllable_count += count_vowels(input_string)
    else: # Else we can just count the vowels
        syllable_count += count_vowels(input_string)

    # If it ends in e but not le then subtract one
    if input_string[-1] == 'e' and input_string[-2] != 'l':
        syllable_count -= 1

    if input_string[-1:-3]
