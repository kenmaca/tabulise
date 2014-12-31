'''
Created on Dec 30, 2014

@author: Kirisanth
'''
from absranker import * 

class LimitedRanker(AbsRanker):
    '''
    classdocs
    '''


    def __init__(self, courses):
        '''
        (Set of Course) -> NoneType
        '''
        AbsRanker.__init__(self, courses)
    
    def _comparekey(x):
        '''
        (Course) -> (int, int)
        Comparator for courses.
        '''
        return len(x.getSections()), len(x.getTutorials()), len(x.getPracticals())
    
    def rank(self):
        '''
        NoneType -> List of courses
        Returns the ranked list.
        '''
        sorted(self._courses, key=self._comparekey)
        return self._courses
        
        
        