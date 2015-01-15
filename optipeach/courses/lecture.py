from . schoolsession import SchoolSession

class Lecture(SchoolSession):
    
    """Represents a single lecture (not a section)"""
    
    def __init__(self, section, timeslot, origin, course):
        """
        (Lecture, str, TimeSlot, str, str) -> NoneType
        """
        super(Lecture, self).__init__(section, timeslot, origin, course, 
                                      section + course + repr(timeslot))
