#!/usr/local/bin/python2.7
""" Counts the number of occurrences for each 311 service category

http://www.michael-noll.com/tutorials/
    writing-an-hadoop-mapreduce-program-in-python/"""
from collections import defaultdict
import csv
import json
import sys

class Reducer(object):
    """ Counts the number of occurrences for each 311 service category"""

    def __init__(self):
        """Reducer class constructor

        Args:
            self: Reducer class handle

        Returns:
            None"""
        self.old_key = None

        self.category_count = defaultdict(int)

        self.service_categories = {'streetmaintenance',
                                   'miscellaneous',
                                   'trashcart',
                                   'buildinghazzard',
                                   'buildingcomplaint',
                                   'repairrequest',
                                   'propertymaintenance',
                                   'defaultrequest',
                                   'propertycomplaint',
                                   'trashcomplaint',
                                   'servicecompliment',
                                   'inspection',
                                   'servicecomplaint',
                                   'buildinginspection',
                                   'buildingcomplaint',
                                   'signmaintenance',
                                   'requestforservice',
                                   'litter',
                                   'recycling',
                                   'treemaintenance',
                                   'metalfurniturecollection',
                                   'yardwaste',
                                   'graffitiremoval',
                                   'deadanimal'}

        self.reset_statistics()

    def reduce(self,
               stdin):
        """Counts the number of occurrences for each 311 service category

        Args:
            self: Reducer class handle

            stdin: Standard input file handle

        Returns:
            None"""
        for fields in csv.reader(stdin, delimiter="\t"):
            this_key = fields[0]

            if self.old_key and self.old_key != this_key:
                self.emit_category_count()

                self.old_key = this_key
                self.reset_statistics()

            self.old_key = this_key
            self.category_count[fields[1]] += 1

        if self.old_key:
            self.emit_category_count()

    def emit_category_count(self):
        """Emits the count for each 311 service category

        Args:
            self: Reducer class handle

        Returns
            None"""
        print "%s\t%s" % (self.old_key,
                          json.dumps(self.category_count))

    def reset_statistics(self):
        """ Resets the category count statistics

        Args:
            self: Reducer class handle

        Returns:
            None"""
        self.category_count.clear()

        for key in self.service_categories:
            self.category_count[key] = 0

def reducer(stdin):
    """Counts the number of occurrences for each 311 service category

    Args:
        stdin: Standard input file handle

    Returns:
        None"""
    reducerobj = Reducer()

    reducerobj.reduce(stdin)

if __name__ == "__main__":
    reducer(sys.stdin)