"""Word Finder: finds random words from a dictionary."""


from torch import randint
import random


class WordFinder:
    def __init__(self, url):
        self.url = url
        self.word_list = self.get_word_list()
        self.word_list_length = len(self.word_list)
        print(f"{self.word_list_length} words read")

    def get_word_list(self):
        file = open(self.url, "r")
        word_list = []
        for line in file:
            word_list.append(line.strip())
        file.close()
        return word_list

    def random(self):
        return self.word_list[random.randint(0, self.word_list_length-1)]


class SpecialWordFinder(WordFinder):
    def __init__(self, url):
        super().__init__(url)

    def special_random(self):
        msg = ""
        while msg == "" or msg.startswith('#'):
            msg = super().random()
        return msg
