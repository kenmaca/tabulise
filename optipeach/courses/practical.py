from . schoolsession import SchoolSession

class Practical(SchoolSession):
    
    """Represents a single practical class."""
    
    def __init__(self, section, timeslot, origin, course):
        """
        (Practical, str, TimeSlot, str, str) -> NoneType
        """
        super(Practical, self).__init__(section, timeslot, origin, course, 
                                      section + course)
