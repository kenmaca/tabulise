class Course():
    def __init__(self, sections, tutorials, practicals, code):
        """
        (Course, set of set of Lecture, set of Tutorial, set of Practical, str) -> Course
        """
        self._sections = sections
        self._tutorials = tutorials
        self._practicals = practicals
        self._code = code
        
    def getSections(self):
        """
        (Course) -> set of set of Lecture
        Return the lecture sections for this Course.
        (Each set within the set is a lecture section.)
        """
        return self._sections
    
    def getTutorials(self):
        """
        (Course) -> set of Tutorial
        Return the tutorial sections for this Course.
        """
        return self._tutorials
    
    def getPracticals(self):
        """
        (Course) -> set of Practical
        Return the practical sections for this Course.
        """
        return self._practicals
    
    def setSections(self, sections):
        """
        (Course, set of set of Lecture) -> NoneType
        Set the lecture sections for this Course.
        (Each set within the set is a lecture section.)
        """
        self._sections = sections
        
    def setTutorials(self, tutorials):
        """
        (Course, set of Tutorial) -> NoneType
        Set the tutorial sections for this Course.
        """
        self._tutorials = tutorials
        
    def setPracticals(self, practicals):
        """
        (Course, set of Practical) -> NoneType
        Set the practical sections for this Course.
        """
        self._practicals = practical

        
    