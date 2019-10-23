def compare(before, after):
    def extract(f):
        for i in open(f):
            if i.startswith('  '):
                yield i.strip()

    bwords = set(extract(before))
    awords = set(extract(after))
    print(len(bwords), len(awords))

    print('Removed:')
    for w in sorted(awords - bwords):
        print(' ', w)
    print('Added:')
    for w in sorted(bwords - awords):
        print(' ', w)


if __name__ == '__main__':
    import sys
    compare(*sys.argv[1:])
