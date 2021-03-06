#!/usr/local/bin/python2.7
""" Counts the number of occurrences for each unique key

http://www.michael-noll.com/tutorials/
    writing-an-hadoop-mapreduce-program-in-python/"""
import csv
import sys


class Reducer(object):
    """ Counts the number of occurrences for each unique key"""

    def __init__(self):
        """Reducer class constructor

        Args:
            self: Reducer class handle

        Returns:
            None"""
        self.old_key = None
        self.key_count = 0

    def reduce(self,
               stdin):
        """Counts the number of occurrences for each unique key

        Args:
            self: Reducer class handle

            stdin: Standard input file handle

        Returns:
            None"""
        for fields in csv.reader(stdin, delimiter="\t"):
            this_key = fields[0]

            if self.old_key and self.old_key != this_key:
                self.emit_key_count()

                self.old_key = this_key
                self.key_count = 0

            self.old_key = this_key
            self.key_count += int(fields[1])

        if self.old_key:
            self.emit_key_count()

    def emit_key_count(self):
        """Counts the number of occurrences for each unique key

        Args:
            self: Reducer class handle

        Returns
            None"""
        print "%s\t%d" % (self.old_key, self.key_count)


def reducer(stdin):
    """Counts the number of occurrences for each unique key

    Args:
        stdin: Standard input file handle

    Returns:
        None"""
    reducerobj = Reducer()
    reducerobj.reduce(stdin)

if __name__ == "__main__":
    reducer(sys.stdin)