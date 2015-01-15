from .. exceptions import ConflictingEventError

class Schedule():
    def __init__(self):
        """
        (Schedule) -> NoneType
        """
        # creating an empty schedule
        # we will use a dictionary to keep track of what blocks are taken
        # the key will be a timeslot and the value will be a block
        self._events = {}
        
    def addEvent(self, block, force=False):
        """
        (Schedule, Block, bool) -> NoneType
        Add the block to set dictionary of current events.
        Will override conflicting blocks if force is True!
        If force is False then an exception will be raised instead (default).
        """
        #removing conflicting blocks if needed
        if force:
            self.removeEvents(block.getTime())
        else:
            #finding conflicts
            for event in self._events.keys():
                if block.getTime().conflictsWith(event):
                    raise ConflictingEvent("Could not schedule event: conflicting with already scheduled event!")
                
        #adding new block
        self._events[block.getTime()] = block
        
        
    def removeEvents(self, time):
        """
        (Schedule, TimeSlot) -> NoneType
        Remove ALL scheduled blocks that conflict with the given TimeSlot.
        """
        #finding conflicting blocks
        for event in self._events.copy().keys():
            if time.conflictsWith(event):
                del(self._events[event])
                
    def getEvents(self, clone=True):
        """
        (Schedule, bool) -> dict of TimeSlot and Block
        Return the dictionary of events if clone if False else return a copy of the events dictionary.
        """
        return self._events.copy() if clone else self._events
        
        