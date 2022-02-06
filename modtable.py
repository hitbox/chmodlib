import argparse

from pathlib import Path

from oct2rwx import oct2rwx

def main(argv=None):
    """
    """
    parser = argparse.ArgumentParser(prog=Path(__file__).stem,
            description=main.__doc__)
    args = parser.parse_args(argv)

    lines = [('Dec', 'Bin', 'RWX')]
    lines += [ (str(i), '{:>03}'.format(bin(i)[2:]), oct2rwx(i)) for i in range(8) ]

    lengths = (tuple(len(v) for v in tup) for tup in lines)
    columns = zip(*lengths)
    maxes = tuple(max(column) for column in columns)

    for tup in lines:
        formatters = list('{:>%s}' % width for width in maxes)
        line = ' '.join(f.format(s) for s, f in zip(tup, formatters))
        print(line)

if __name__ == '__main__':
    main()
