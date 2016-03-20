from csv import DictReader
from dateutil import parser
import re

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

        self.readerobj = DictReader(h_file, fieldnames)

    def parse(self):
        """ Parses a Cincinnati 311 CSV file record

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
                record[key] = parser.parse(record[key])

            for key in self.string_fields:
                record[key] = re.sub("\"", "", record[key].lower())

        return record
