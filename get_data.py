def convert_syllables_to_json
    with open("Syllables.txt", encoding="cp1252") as syll_data:
        raw_file_text = syll_data.read().split("\n")
        del(raw_file_text[-1])
        syllable_dictionary = [ {"word": line.split("=")[0], "count": get_count_from_line(line) } for line in raw_file_text]
        print(json.dumps(syllable_dictionary))

def get_count_from_line(line):
    syllable_line = line[line.index("=")+1:len(line)]
    return len(syllable_line.split("·"))
