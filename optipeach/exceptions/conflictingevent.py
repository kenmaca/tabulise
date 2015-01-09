class ConflictingEvent(Exception):
    '''Raised when the user has tried to schedule a block that conflicts with an already scheduled block.'''
    pass