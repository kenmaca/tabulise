class Block():
    """
    This is an abstract class.  Do not instantiate!
    """
    def __init__(self, id, course, timeslot, origin):
        """
        (Block, str, str, TimeSlot, str) -> Block
        """
        self._id = id
        self._course = course
        self._time = timeslot
        self._origin = origin
        
    def getId(self):
        """
        (Block) -> str
        Return the id of this Block.
        """
        return self._id
    
    def getCourse(self):
        """
        (Block) -> str
        Return the course to which this class belongs.
        """
        return self._course
    
    def getTime(self):
        """
        (Block) -> TimeSlot
        Return the TimeSlot that this Block occupies.
        """
        return self._time
    
    def getOrigin(self):
        """
        (Block) -> str
        Return the Origin of this block (the string from the csv).
        """
        return self._origin
    
    def setId(self, id):
        """
        (Block, str) -> NoneType
        Set the id of this Block.
        """
        self._id = id
        
    def setCourse(self, course):
        """
        (Block, str) -> NoneType
        Set the course to which this Block belongs.
        """
        self._course = course
        
    def setTime(self, time):
        """
        (Block, str) -> NoneType
        Set the time of this Block.
        """
        self._time = time
        
    def setOrigin(self, origin):
        """
        (Block, str) -> NoneType
        Set the origin of this Block.
        """
        self._origin = origin
