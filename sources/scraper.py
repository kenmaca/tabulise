import requests

class Scraper:
    ''' An basic Scraper used primarily to extend other more specialized
    Scrapers. '''
    
    def pull(self, url, args = {}):
        ''' (str, [{str : {str : str}}]) -> str
        Retrieves HTML from the website at url via GET for further processing. 
        If args is specified, then POST will be used in place of GET (for 
        passing in form values).
        
        REQ: args should be in the format {'form':{'key1':'value', ...}, ...}
        '''
        return requests.get(url) if args else requests.post(url, data = args)