from . schoolsession import SchoolSession

class Tutorial(SchoolSession):
    def __init__(self, section, timeslot, origin, course):
        super(Lecture, self).__init__(section, timeslot, origin, course, 
                                      section + course)
