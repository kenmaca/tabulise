class Block():
    """
    This is an abstract class.  Do not instantiate!
    """
    def __init__(self, id, course, timeslot):
        """
        (Class, str, str, TimeSlot) -> Class
        """
        self._id = id
        self._course = course
        self._time = timeslot
        
    def getId(self):
        """
        (Class) -> str
        Return the id of this Class.
        """
        return self._id
    
    def getCourse(self):
        """
        (Class) -> Course
        Return the Course to which this class belongs.
        """
        return self._course
    
    def getTime(self):
        """
        (Class) -> TimeSlot
        Return the TimeSlot that this Class occupies.
        """
        return self._time
    
    def setId(self, id):
        """
        (Class, str) -> NoneType
        Set the id of this Class.
        """
        self._id = id
        
    def setCourse(self, course):
        """
        (Class, Course) -> NoneType
        Set the Course to which this Class belongs.
        """
        self._course = course
        
    def setTime(self, time):
        """
        (Class, str) -> NoneType
        Set the time of this Class.
        """
        self._time = time
