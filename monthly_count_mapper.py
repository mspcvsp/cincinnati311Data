#!/usr/local/bin/python2.7
""" Parses a set of Cincinnati 311 records and emits the following
(key, value) pair:

<Year>-<Month>-<01> 1

http://www.michael-noll.com/tutorials/
    writing-an-hadoop-mapreduce-program-in-python/"""
from Cincinnati311CSVDataParser import Cincinnati311CSVDataParser
import sys


def mapper(stdin):
    """ Parses a set of Cincinnati 311 records and emits the following
    (key, value) pair:

    <Year>-<Month>-<01> 1

    Args:
        stdin: Standard input file handle

    Returns:
        None"""

    parserobj = Cincinnati311CSVDataParser(stdin)

    for record in parserobj:
        if record != None:
            print "%d-%d-01\t1" % (record['requesteddatetime'].year,
                                   record['requesteddatetime'].month)

if __name__ == "__main__":
    mapper(sys.stdin)