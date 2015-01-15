from . schoolsession import SchoolSession

class Tutorial(SchoolSession):
    
    """Represents a single tutorial class."""
    
    def __init__(self, section, timeslot, origin, course):
        """
        (Tutorial, str, TimeSlot, str, str) -> NoneType
        """
        super(Tutorial, self).__init__(section, timeslot, origin, course, 
                                      section + course)
