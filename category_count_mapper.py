#!/usr/local/bin/python2.7
""" Parses a set of Cincinnati 311 records and emits the following
(key, value) pair:

<Year>-<Month> <servicecategory>

http://www.michael-noll.com/tutorials/
    writing-an-hadoop-mapreduce-program-in-python/"""
from Cincinnati311CSVDataParser import Cincinnati311CSVDataParser
from ServiceCodeCategory import ServiceCodeCategory
import sys


def mapper(stdin):
    """ Parses a set of Cincinnati 311 records and emits the following
    (key, value) pair:

    <Year>-<Month> <servicecategory>

    Args:
        stdin: Standard input file handle

    Returns:
        None"""

    parserobj = Cincinnati311CSVDataParser(stdin)

    mapobj = ServiceCodeCategory()

    for record in parserobj:

        if record is not None:

            print "%d-%d-01\t%s" % (record['requesteddatetime'].year,
                                    record['requesteddatetime'].month,
                                    mapobj.lookup_service_category(record))

if __name__ == "__main__":
    mapper(sys.stdin)