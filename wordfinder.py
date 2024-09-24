import random

"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    def __init__(self, path):
        """Read dict and reports the number of items read"""

        dict_file = open(path)
        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """list of words"""

        return [w.strip() for w in dict_file]

    def random(self):
        """Return a random word"""

        return random.choice(self.words)


class SpecialWordFinder(WordFinder):

    def parse(self, dict_file):
        """gives a list of words, skipping the comments."""

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]