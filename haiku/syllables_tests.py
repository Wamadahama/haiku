import unittest
import syllables

# def test_upper(self):
    # self.assertEqual('foo'.upper(), 'FOO')
class TestSyllablesMethods(unittest.TestCase):

    def test_is_vowel(self):
        self.assertEqual(syllables.is_vowel("A"), True)

    def test_count_vowels(self):
        self.assertEqual(syllables.count_vowels("AEIOU"), 5)

    def test_contiguous_vowel_count(self):
        self.assertEqual(syllables.contiguous_vowel_count("RREEFFAA"), 2)

    def test_ends_in(self):
        self.assertEqual(syllables.ends_in("feel", "el"), True)
        self.assertEqual(syllables.ends_in("feel", "le"), False)

if __name__ == '__main__':
    unittest.main()
