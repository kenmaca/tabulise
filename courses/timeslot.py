class TimeSlot():
    def __init__(self, start, end, semester):
        """
        (TimeSlot, str, str, str) -> TimeSlot
        REQ: start and end must be formatted in 24 hour time beginning with
        the first 3 letters of the day (eg. "TUE 12:00") and semester should be either "Y", "F", "S"
        """
        self._start = start
        self._end = end
        self._semester = semester
        
    def __repr__(self):
        """
        (TimeSlot) -> str
        Return a string representation of the TimeSlot in the form "DAY HH:MM->DAY HH:MM S"
        """
        return self._start + "->" + self._end + " " + self._semester
    
    def getStart(self):
        """
        (TimeSlot) -> str
        Return the start time.
        """
        return self._start
    
    def getEnd(self):
        """
        (TimeSlot) -> str
        Return the end time.
        """
        return self._end
    
    def setStart(self, start):
        """
        (TimeSlot, str) -> NoneType
        Changes the start time to start
        REQ: start must be in the same format as __init__
        """
        self._start = start
        
    def setEnd(self, end):
        """
        (TimeSlot, str) -> NoneType
        Changes the start time to start
        REQ: end must be in the same format as __init__
        """
        self._end = end
