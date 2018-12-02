#!/usr/bin/env python

from __future__ import print_function

import os

INPUT_DIR = os.path.abspath('in')
OUTPUT_DIR = os.path.abspath('out')
INPUT_FILE = os.path.join(INPUT_DIR, 'input.txt')
OUTPUT_FILE = os.path.join(OUTPUT_DIR, 'out.txt')


def main():
    print("CONT: running main.py (without root!)...")
    os.listdir(INPUT_DIR)
    with open(INPUT_FILE, 'r') as f:
        print("CONT: read input data:\n'{}'".format(f.read()))

    with open(OUTPUT_FILE, 'w+') as f:
        f.write("hello host, I'm the container!")

    with open(OUTPUT_FILE, 'r') as f:
        print("CONT: read back content:\n'{}'".format(f.read()))
        print('\tat path: {}'.format(OUTPUT_FILE))


if __name__ == '__main__':
    main()
