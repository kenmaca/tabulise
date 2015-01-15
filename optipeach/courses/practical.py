from . schoolsession import SchoolSession

class Practical(SchoolSession):
    def __init__(self, section, timeslot, origin, course):
        super(Lecture, self).__init__(section, timeslot, origin, course, 
                                      section + course)
