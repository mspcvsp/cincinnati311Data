from csv import DictReader
from dateutil import parser
import re
import string

class Cincinnati311CSVDataParser(object):
    """ Class that parses and cleans a Cincinnati 311 Comma Seperated Value
    (CSV) file record

    Data set description:
    --------------------
    https://data.cincinnati-oh.gov/Thriving-Healthy-Neighborhoods/
        Cincinnati-311-Non-Emergency-Service-Requests/4cjh-bm8b/about"""

    def __init__(self,
                 h_file):
        """ Cincinnati311CSVDataParser class constructor

        Args:
            self: Cincinnati311CSVDataParser class object handle

            h_file: Cincinnati 311 csv file handle

        Returns:
            None"""
        fieldnames = ['jurisdictionid',
                      'servicerequestid',
                      'status',
                      'statusnotes',
                      'servicename',
                      'servicecode',
                      'description',
                      'agencyresponsible',
                      'servicenotice',
                      'requesteddatetime',
                      'updateddatetime',
                      'expecteddatetime',
                      'address',
                      'addressid',
                      'zipcode',
                      'latitude',
                      'longitude',
                      'requesteddate',
                      'updateddate',
                      'lasttableupdate']

        matchobj = re.compile('.*date.*')

        self.date_fields = filter(lambda elem: matchobj.match(elem) != None,
                                  fieldnames)

        self.string_fields = filter(lambda elem: matchobj.match(elem) == None,
                                    fieldnames)

        # http://stackoverflow.com/questions/265960/
        #   best-way-to-strip-punctuation-from-a-string-in-python
        self.punctuation_table = table = string.maketrans("", "")

        self.readerobj = DictReader(h_file, fieldnames)

    def __iter__(self):
        """ Iterator
        :return: None
        """
        return self

    def next(self):
        """ Parses a Cincinnati 311 CSV file record

        http://stackoverflow.com/questions/19151/how-to-make-class-iterable

        Args:
            self: Cincinnati311CSVDataParser class object handle

        Returns:
            record: Dictionary that stores a Cincinnati 311 data CSV file
                    record"""
        record = self.readerobj.next()

        if record['jurisdictionid'] == 'JURISDICTION_ID':
            record = None
        else:
            for key in self.date_fields:
                if len(record[key]) > 0:
                    record[key] = parser.parse(record[key])

            for key in self.string_fields:
                record[key] = re.sub("\"", "", record[key].lower())

            if len(record['servicecode']) > 0:
                record['servicecode'] =\
                    re.sub("\s+", "", record['servicecode'])

                record['servicecode'] =\
                    record['servicecode'].translate(self.punctuation_table,
                                                    string.punctuation)

                record['servicename'] =\
                    record['servicename'].translate(self.punctuation_table,
                                                    string.punctuation)

        return record
