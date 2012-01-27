#!/usr/bin/python

def next_case():
    """A generator that returns the next case to be reversed"""

    f = open('input.txt', 'r')
    num_of_cases = int(f.readline())

    for i in range(num_of_cases):
        yield f.readline().strip()

if __name__ == '__main__':
    i = 1
    for sentence in next_case():
        words = sentence.split()
        print "Case #" + str(i) + ':',
        print " ".join(reversed(words))
        i += 1
