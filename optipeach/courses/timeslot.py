from .. exceptions import InvalidTimeError


class TimeSlot():
    
    """Represents a period of time in a weekly schedule."""
    
    def __init__(self, start, end, semester):
        """
        (TimeSlot, str, str, str) -> TimeSlot
        REQ: start and end must be formatted in 24 hour time beginning with
        the first 2 letters of the day (eg. "TU 12:00") and semester should match
        timeslots occurring in the same semester.
        """
        if not (self._checkTime(start) and self._checkTime(end)):
            raise InvalidTime("You have entered a time that was not in the format 'TU 12:00'!")
        self._start = start
        self._end = end
        self._semester = semester
        
    def __repr__(self):
        """
        (TimeSlot) -> str
        Return a string representation of the TimeSlot in the form "DAY HH:MM->DAY HH:MM S"
        """
        return "%s%s%s %s" % (self._start, "->", self._end, self._semester)
    
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
        if not self._checkTime(start):
            raise InvalidTime("You have entered a time that was not in the format 'TU 12:00'!")
        self._start = start
        
    def setEnd(self, end):
        """
        (TimeSlot, str) -> NoneType
        Changes the start time to start
        REQ: end must be in the same format as __init__
        """
        if not self._checkTime(end):
            raise InvalidTime("You have entered a time that was not in the format 'TU 12:00'!")
        self._end = end
        
    def conflictsWith(self, other):
        """
        (TimeSlot, TimeSlot) -> bool
        Return True if other TimeSlot overlaps with this TimeSlot.
        """
        #checking if they have the same start time
        if self._start == other._start:
            return True
        
        #finding which starts first
        if self._startsBefore(self._start, other._start):
            lesser, greater = self, other
        else:
            lesser, greater = other, self
            
        #checking if lesser ends before greater starts
        if lesser._startsBefore(lesser._end, greater._start):
            return False
        return True

    @staticmethod            
    def _startsBefore(time, time2):
        """
        (TimeSlot, str, str) -> bool
        Return True if time happens before time2
        REQ times must be of the format "TU 12:00"
        >>> TimeSlot._startsBefore("TU 12:00", "MO 16:00")
        True
        >>> TimeSlot._startsBefore("TU 12:00", "TU 11:00")
        False
        """
        #checking times are valid
        if not (self._checkTime(time) and self._checkTime(time2)):
            raise InvalidTime("You have entered a time that was not in the format 'TU 12:00'!")
        
        day_order = {"SU": 0, "MO": 1, "TU": 2, "WE": 3, "TH": 4, "FR": 5, "SA": 7}
        
        #checking which start time is earlier
        if day_order[time[:2]] < day_order[time2[:2]]:
            return True
        elif day_order[time[:2]] > day_order[time2[:2]]:
            return False
        
        #time slots have same start day, must check hours
        if int(time[3:5]) < int(time2[3:5]):
            return True
        elif int(time[3:5]) > int(time2[3:5]):
            return False
        
        #timeslots have same start hours, must check minutes
        if int(time[6:8]) < int(time2[6:8]):
            return True
        return False
        
        
        
    
    @staticmethod
    def _checkTime(time):
        """
        (TimeSlot, str) -> bool
        Return True if the time is in a valid format.
        eg. "TU 12:00"
        """
        #_partial is used to create elements like "00", "01", ..., "09"
        _partial = {"0" + str(i) for i in range(10)}
        days = {"SU", "MO", "TU", "WE", "TH", "FR", "SA"}
        hours = _partial.union({str(i) for i in range(10,24)})
        minutes = _partial.union({str(i) for i in range(10, 60)})
        return (time[:2] in days and time[3:5] in hours and
                time[6:8] in minutes)
