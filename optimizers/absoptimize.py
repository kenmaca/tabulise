'''
Created on Dec 30, 2014

@author: Kirisanth
'''
import sys
import os

# add local packages to Python path
path = os.path.abspath(os.path.dirname(__file__))
for subdir in ["/.."]:
    if not (path + subdir) in sys.path:
        sys.path.insert(0, os.path.abspath(path + subdir))
del subdir

import exceptions

class AbsOptimize(object):
    '''
    classdocs
    '''

    def __init__(self, courses):
        '''
        (Set of Course) -> NoneType
        '''
        self._courses = list(courses)
        
    def MoveToTop(self, course):
        '''
        (Course) -> NoneType
        Finds and moves the given course to the top.
        '''
        self.swapRank(self._courses.index(course), 0)
    
    def MoveToBottom(self, course):
        '''
        (Course) -> NoneType
        Finds and moves the given course to the bottom.
        '''
        self.swapRank(self._courses.index(course), len(self._courses) - 1)
    
    def swapRank(self, i, new_i):
        '''
        (int, int) -> NoneType
        Swaps the rank of the course to the new rank.
        '''
        self._courses[i], self._courses[new_i] = self._courses[new_i], self._courses[i]

    def rank(self):
        '''
        Returns the ranking of the courses. Since this is Abstract NotImplementError is raised.
        '''
        raise NotImplementedError

        
