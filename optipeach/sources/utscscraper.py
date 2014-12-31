import scraper
from lecture import *
from tutorial import *
from practical import *
from timeslot import *
import requests
import csv

# two placeholders % (first % is discipline, second is session)
URL = 'https://www.utsc.utoronto.ca/~registrar/timetable_src/export.php?&\
submit&course=%s&sess=%s'

# CSV settings
CSV_QUOTE_CHAR = '"'
CSV_DELIMITER = ','

# TimeSlot settings
TIMESLOT_CURRENT_YEAR = '2014'
TIMESLOT_DAY_FORMAT = '%s %s'
TIMESLOT_SEMESTER_FORMAT = '%s%s' + TIMESLOT_CURRENT_YEAR

class UTSCScraper(scraper.Scraper):
    ''' A scraper used to pull all courses from the UTSC Registrar's Office
    Course listing page found at 
    https://www.utsc.utoronto.ca/~registrar/scheduling/timetable. '''
    
    @classmethod
    def pullAllBlocks(cls, disciplines, sessions = ['summer', 'year']):
        ''' (list of str[, list of str]) -> list of Block
        Grabs all available Blocks from the Course listing page. Each Block
        represents either a lecture, tutorial, or practical timeslot.
        
        REQ: disciplines are all the 3-letter programs found in Step 2.
        
        REQ: sessions are all the academic periods in Step 1. Standard values
        are ['summer', 'year'].
        '''
        
        # outer listcomp used to flatten 2d list, inner for cartesian product
        # of disciplines and sessions
        return [block for block_list in 
                [cls.pullBlocks(discipline, session) for discipline in 
                 disciplines for session in sessions] for block in block_list]
    
    @classmethod
    def pullBlocks(cls, discipline, session):
        ''' (str, str) -> list of Block
        Grabs all Blocks from a certain discipline and session.
        '''
        
        # cut off the header line
        return [cls.toBlock(line, session) for line in 
                super(UTSCScraper, cls).pull(URL % (discipline, session))[1:]]
    
    @classmethod
    def toBlock(cls, line, session):
        ''' (str, session) -> Block
        Converts a single CSV line to a respective Block object.
        
        >>> UTSCScraper.toBlock('"CSCA08H3 F","LEC01","W,I","MO","12:00",\
        "13:00","AA 112","B.Harrington",""')
        <Block object at ..>
        '''
        
        # needs csv as elements are wrapped in quotes and we need to ignore
        # commas inside quotation marks
        block_data = list(csv.reader(line.splitlines(), 
                                     quotechar = CSV_QUOTE_CHAR, 
                                     delimiter = CSV_DELIMITER, 
                                     quoting = csv.QUOTE_ALL, 
                                     skipinitialspace = True))[0]
        
        # determine what Block obj to instantiate by id[:3]
        return {'LEC': Lecture, 
                'L01': Lecture, 
                'L31': Lecture, 
                'TUT': Tutorial, 
                'T01': Tutorial, 
                'PRA': Practical
                }[block_data[1].strip()[:3]](block_data[1], block_data[0][:-2], 
                                             TimeSlot(TIMESLOT_DAY_FORMAT % 
                                                      (block_data[3], 
                                                       block_data[4]), 
                                                      TIMESLOT_DAY_FORMAT % 
                                                      (block_data[3], 
                                                       block_data[5]), 
                                                      TIMESLOT_SEMESTER_FORMAT %
                                                      (session, 
                                                       block_data[0][-1])), 
                                             block_data)