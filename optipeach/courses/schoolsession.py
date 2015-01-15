from . block import Block

class SchoolSession(Block):
    
    """This class is used to represent all university classes."""
    
    def __init__(self, section, timeslot, origin, course, id):
        """
        (SchoolSession, str, TimeSlot, str, str) -> NoneType
        """
        super(SchoolSession, self).__init__(id, timeslot, origin)
        self._section = section
        self._course = course
        
    def getSection(self):
        """
        (SchoolSession) -> str
        Return the section id of this SchoolSession.
        """
        return self._section
    
    def getCourse(self):
        """
        (SchoolSession) -> str
        Return the course id of this SchoolSession.
        """
        return self._course
    
    def setSection(self, section):
        """
        (SchoolSession, str) -> NoneType
        """
        self._section = section
        
    def setCourse(self, course):
        """
        (SchoolSession, str) -> NoneType
        """
        self._course = course
