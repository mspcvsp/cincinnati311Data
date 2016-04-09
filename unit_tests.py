#!/usr/local/bin/python2.7
"""
City of Cincinnati 311 Open Data Analysis Software Unit Tests

http://www.jeffknupp.com/blog/2013/12/09/
    improve-your-python-understanding-unit-testing/

https://docs.python.org/2/library/unittest.html

http://nbviewer.ipython.org/gist/jacebrowning/6587691
"""
import csv
from collections import defaultdict
import json
import subprocess
import unittest

class TestCategoryCountReducer(unittest.TestCase):

    """ Category count reducer unit test

    Args:
        self: TestCategoryCountReducer class handle

    Returns:
        None"""
    def test_category_count(self):
        # Initialize the reducer expected output
        system_cmd = "cat ./Data/sample1000.csv | " +\
                     "./category_count_mapper.py | sort"

        #http://www.cyberciti.biz/faq/
        #    python-run-external-command-and-get-output/
        stdout = subprocess.Popen(system_cmd,
                                  shell=True,
                                  stdout=subprocess.PIPE).stdout

        expected_output = {}

        for fields in csv.reader(stdout, delimiter="\t"):

            if not expected_output.has_key(fields[0]):
                expected_output[fields[0]] = defaultdict(int)

            expected_output[fields[0]][fields[1]] += 1

        # Generate the reducer output
        reducer_output = {}

        system_cmd = "cat ./Data/sample1000.csv | " +\
                     "./category_count_mapper.py | sort | " +\
                     "./category_count_reducer.py"

        stdout = subprocess.Popen(system_cmd,
                                  shell=True,
                                  stdout=subprocess.PIPE).stdout

        for fields in csv.reader(stdout, delimiter="\t"):
            raw_counts = json.loads(fields[1])

            for key in raw_counts.keys():
                if raw_counts[key] == 0:
                    raw_counts.pop(key)

            reducer_output[fields[0]] = raw_counts

        self.assertTrue(expected_output == reducer_output)

if __name__ == "__main__":
    unittest.main()
