import string

WIKI_BESTAND = '/Users/tom/Downloads/\
nlwiktionary-20191001-pages-articles-multistream-index.txt'
WOORD_BESTAND = 'woord-frequenties.txt'
SLECHT_BESTAND = 'slechte-woorden.txt'

BLACKLIST = {i.strip() for i in open(SLECHT_BESTAND)}
AANTAL = 1000000000000000

MIN = 4
MIN_ACHTERVOEGSEL = 4
VOORVOEGSELS = (
    'aan',
    'achter',
    'af',
    'be',
    'bij',
    'binnen',
    'door',
    'er',
    'goed',
    'her',
    'in',
    'los',
    'mee',
    'mis',
    'na',
    'neer',
    'om',
    'onder',
    'ont',
    'op',
    'over',
    'samen',
    'tegen',
    'teleur',
    'toe',
    'uit',
    'vast',
    'ver',
    'vol',
    'voor',
    'vrij',
    'weer',
    'weg',
    'zwart',
)

is_woord = set(string.ascii_lowercase).issuperset


def wikitionary():
    for lijn in open(WIKI_BESTAND):
        _, _, woord = lijn.strip().split(':', maxsplit=2)
        if is_woord(woord):
            yield woord


def freq():
    for lijn in open(WOORD_BESTAND):
        woord, _ = lijn.strip().rsplit(maxsplit=1)
        yield woord



def werkwoorden(woorden):
    alle = set()
    resultaat = {}

    for woord in woorden:
        if not (woord.endswith('en') or woord.endswith('gaan')):
            continue

        alle.add(woord)
        for v in VOORVOEGSELS:
            if not woord.startswith(v):
                continue

            achtervoegsel = woord[len(v):]
            if len(achtervoegsel) < MIN_ACHTERVOEGSEL:
                continue

            if achtervoegsel.startswith('ge') and achtervoegsel != 'geven':
                continue

            if achtervoegsel in BLACKLIST:
                continue

            resultaat.setdefault(achtervoegsel, []).append(woord)

    for achtervoegsel, lijst in resultaat.items():
        if achtervoegsel in alle:
            lijst.append(achtervoegsel)
        lijst.sort()

    resultaat = {k: v for k, v in resultaat.items() if len(v) > 1}
    return sorted(resultaat.items(), key=lambda v: len(v[1]), reverse=True)


def druck_werkwoorden(werkwoorden):
    for i, (k, v) in enumerate(werkwoorden):
        print(k)
        if not False:
            for j in v:
                print(' ', j)
            print()
        if i > AANTAL:
            break


if __name__ == '__main__':
    druck_werkwoorden(werkwoorden(wikitionary()))
