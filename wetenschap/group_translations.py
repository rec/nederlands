def group_translations(fname):
    lines = [i.strip() for i in open(fname)]
    assert len(lines) % 2 == 0, len(lines)
    l2 = len(lines) // 2
    for e, d in zip(lines[:l2], lines[l2:]):
        if e == d:
            continue
        ewords = e.split()
        if ewords[0] == 'the':
            dwords = d.split()
            # if dwords[0] in ('de', 'het'):
            if dwords[0] == 'de':
                if dwords[1:] == ewords[1:]:
                    continue
        print(e + ',', d)


if __name__ == '__main__':
    import sys

    for f in sys.argv[1:]:
        group_translations(f)
