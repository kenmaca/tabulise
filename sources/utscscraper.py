import requests

class UTSCScraper(Scraper):
    ''' A scraper used to pull all courses from the UTSC Registrar's Office
    Course listing page found at 
    https://www.utsc.utoronto.ca/~registrar/scheduling/timetable. '''
    
    def pull(self, disciplines, sessions = ['summer', 'year']):
        ''' (list of str[, list of str]) -> list of Blocks
        Grabs all available Blocks from the Course listing page. Each Block
        represents either a lecture, tutorial, or practical timeslot.
        
        REQ: disciplines are all the 3-letter programs found in Step 2.
        
        REQ: sessions are all the academic periods in Step 1. Standard values
        are ['summer', 'year'].
        '''
        
        pass
    
    def toBlock(self, line):
        ''' (str) -> Block
        Converts a single CSV line to a respective Block object.
        
        >>> UTSCScraper.toBlock('"CSCA08H3 F","LEC01","W,I","MO","12:00",\
        "13:00","AA 112","B.Harrington",""')
        <Block object at ..>
        '''
        
        pass