class Schedule():
    def __init__(self):
        """
        (Schedule) -> NoneType
        """
        # creating an empty schedule
        # we will use a dictionary to keep track of what blocks are taken
        # the key will be a timeslot and the value will be a block
        events = {}