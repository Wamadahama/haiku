def is_vowel(character):
    """Determines whether a character is a vowel or not """
    vowels = ["A", "E", "I", "O", "U"]
    if character.upper() in vowels:
        return True
    else:
        return False

def count_vowels(search_string):
    """Counts the vowels in a string """
    count = 0
    for _,character in enumerate(search_string):
        if is_vowel(character):
            count += 1
    return count

def contiguous_vowel_count(search_string):
    """ Determines if there is contiguous vowels in a search string and if there is then search it"""
    last_char = ''
    counter = 0

    for _,character in enumerate(search_string):
        if is_vowel(character) and is_vowel(last_char):
            counter += 1

        last_char = character
    return counter

def half_contiguous(i):
    """if i is even return i / 2, if i is odd return i % 2"""
    if i % 2 == 0 :
        return (i / 2)
    else:
        return (i % 2)

def ends_in(search_string, sub_string):
    """Determines whether a string ends in a certain substring"""
    end_characters = search_string[-len(sub_string):]

    if end_characters == sub_string:
        return True
    else:
        return False

def count_syllables(input_string):
    """Estimates the syllable count for a word"""
    input_string = input_string.strip().lower()

    if len(input_string) == 0:
        return 0

    if len(input_string) == 1:
        return 1

    syllable_count = count_vowels(input_string)

    if ends_in(input_string, "ian"):
        contiguous_count =  (contiguous_vowel_count(input_string) - 1)
        syllable_count -= half_contiguous(contiguous_count)
    else:
        contiguous_count =  (contiguous_vowel_count(input_string))
        syllable_count -= half_contiguous(contiguous_count)

    if ends_in(input_string, "e") and not ends_in(input_string, "le") and input_string != "the":
        syllable_count -= 1

    if ends_in(input_string, "ed") and input_string[-3].upper() not in ['t','i','e']:
        syllable_count -= 1

    if ends_in(input_string, "es") and input_string[-3].upper() not in ['t','i','e']:
        syllable_count -= 1

    return int(syllable_count)
