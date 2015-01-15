class ConflictingEventError(Exception):
    '''Raised when the user has tried to schedule a block that conflicts with an already scheduled block.'''
    pass

class InvalidTimeError(Exception):
    '''Raised when the user has entered an invalid time.'''
    pass

class DuplicateBlockError(Exception):
    '''Raised when the user tries to instantiate a block with an already existing ID.'''
    pass