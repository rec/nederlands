import random
import string
import sys
import yaml

FILES = '/code/nederlands/wiki-100k.txt'
LETTERS = set(string.ascii_lowercase)
VOWELS = set('aeiouy')
COUNT = 10
LENGTH = 23
CUTOFF = 2000

def read_words():
    word_list = []
    words = set()
    counts = {}

    for line in open(FILES):
        word = line.strip().lower()
        if not LETTERS.issuperset(word):
            continue
        if not VOWELS.intersection(word):
            continue
        if word in BANNED_LIST:
           continue
        if word in words:
            continue
        if len(word) == '1' and word not in 'ai':
            continue

        word_list.append(word)
        words.add(word)
        # print(word)

    word_list = word_list[:CUTOFF]
    for i in range(COUNT):
        names = []
        length = 0
        while length < LENGTH:
            word = random.choice(word_list)
            length += len(word)
            names.append(word)

        print(*names, sep='-')


BANNED_LIST = {
    'gutenberg',
    'ne',
    'de',
    'il',
    'le',
    'et',
    'mr',
    'que',
    'en',
    'def',
    'du',
    'der',
    'das',
    'dem',
    'des',
    'het',
}



if __name__ == '__main__':
    read_words()
