'''
Created on Dec 30, 2014

@author: Kirisanth
'''
from absoptimize import AbsOptimize

class LimitedOptimize(AbsOptimize):
    '''
    classdocs
    '''


    def __init__(self, courses):
        '''
        (Set of Course) -> NoneType
        '''
        AbsOptimize.__init__(courses)
    
    def _comparekey(self, x):
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
        
        
        