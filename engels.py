import string

WIKI_BESTAND = '/Users/tom/Downloads/\
enwiktionary-20191020-pages-articles-multistream-index.txt'
is_woord = set(string.ascii_lowercase).issuperset
is_hex = set('abcdef').issuperset


def wikitionary():
    for lijn in open(WIKI_BESTAND):
        _, _, woord = lijn.strip().split(':', maxsplit=2)
        if is_woord(woord):
            yield woord


def hex_woorden():
    counts = [0, 0]
    for woord in wikitionary():
        counts[is_hex(woord)] += 1
    print(counts[1], '/', counts[0], '=', counts[1] / counts[0])


if __name__ == '__main__':
    classic_extract()
