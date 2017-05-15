#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This script provides a "NATO" alphabet or phonetic
pronunciation of alphanumeric characters as commonly
used in radio-telephony and similar scenarios.
"""

import os
import string
from sys import argv, exit

from pardon.mappings import word_mapping, number_mapping

def help_text():
    text = \
        """help:
    utility script to translate alphanumeric characters
    into phonetic spelling as defined by NATO alphabet standards"""
    print("usage: {0} string ...".format(
        os.path.basename(argv[0])))
    print(text)
    exit(1)


def translate(thing):
    result = list()
    for character in str(thing.lower()):
        if character in string.ascii_lowercase:
            result.append(word_mapping[character])
        elif character in string.digits: # string.digits returns a string of digits so we don't need to convert
            result.append(number_mapping[character])
        else:
            result.append(character)
    return result


def main():
    if len(argv) < 2 or '--help' in argv:
        help_text()
    else:
        for i in argv[1:]:
            print("\"{}\"".format(i))
            print("\n\t", end="") # TODO: this is purely a formatting element, may be better addressed in another way
            for item in translate(i):
                print(item, end="  ")
            print(end="\n\n")
    exit(0)

if __name__ == "__main__":
    main()
