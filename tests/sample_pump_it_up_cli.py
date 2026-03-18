#!/usr/bin/env python3


def pump_it_up(input):
    return input + 100


def main(argv):
    if not argv:
        print('No pump')
    else:
        print(pump_it_up(int(argv[0])))


if __name__ == '__main__':
    import sys

    main(sys.argv[1:])
