from .. exceptions import DuplicateBlockError


class Block():
    """
    This is an abstract class.  Do not instantiate!
    This represents a single event (recurring) on a weekly schedule.
    """
    
    _block_list = set()
    
    def __init__(self, id, timeslot, origin):
        """
        (Block, str, str, TimeSlot, str) -> NoneType
        """
        self._id = id
        self._time = timeslot
        self._origin = origin
        Block.addBlock(id)

    def __repr__(self):
        ''' (Block) -> str '''

        return self.getCourse() + ' ' + self.getId()
        
    def getId(self):
        """
        (Block) -> str
        Return the id of this Block.
        """
        return self._id
    
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
        
    @staticmethod
    def addBlock(block_id):
        """
        (Block) -> NoneType
        Add the block to the static list of blocks.
        """
        if block_id in Block._block_list:
            raise DuplicateBlockError("A block with the same ID already exists!")
        else:
            Block._block_list.add(block_id)
