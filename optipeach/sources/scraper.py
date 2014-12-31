import requests

# default line encoding is unicode (utf-8)
DECODE_TYPE = 'utf-8'

class Scraper:
    ''' An basic Scraper used primarily to extend other more specialized
    Scrapers. '''
    
    @classmethod
    def pull(cls, url, args = {}):
        ''' (str, [{str : {str : str}}]) -> list of str
        Retrieves a list of lines from the website at url via GET for 
        further processing. If args is specified, then POST will be used in 
        place of GET (for passing in form values).
        
        REQ: args should be in the format {'form':{'key1':'value', ...}, ...}
        '''

        # removes all newline chars and the trailing empty line at the end        
        return [line.strip() for line in 
                (requests.get(url) if args else 
                 requests.post(url, data = args))
                .text.split('\r\n')][:-1]