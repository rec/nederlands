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


def schrijf_alles():
    for woord in wikitionary():
        print(woord)


def hex_woorden(woorden):
    counts = [[0, 0], [0, 0]]
    for woord in woorden:
        woord = woord.strip()
        seven = len(woord) == 7
        hx = is_hex(woord)
        counts[seven][hx] += 1
        if hx:
            print('!' if seven else ' ', woord)

        # acceded
        # deceded
        # defaced
        # effaced

    for c in counts:
        print(c[1], '/', c[0], '=', c[1] / c[0])


if __name__ == '__main__':
    hex_woorden(open('engelse_woorden.txt'))
    # hex_woorden(wikitionary())
    # schrijf_alles()
