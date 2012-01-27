#!/usr/bin/python

import sys

def next_case(file_name):
    """A generator that returns the next case to be reversed"""

    f = open(file_name, 'r')
    num_of_cases = int(f.readline())

    for i in range(num_of_cases):
        yield f.readline().strip()

if __name__ == '__main__':
    i = 1
    for sentence in next_case(sys.argv[1]):
        words = sentence.split()
        print "Case #" + str(i) + ':',
        print " ".join(reversed(words))
        i += 1
