class Course():
    def __init__(self, sections, tutorials, practicals, code):
        """
        (Course, dict of string and set of Lecture, set of Tutorial, set of Practical, 
        str) -> Course
        sections should be of the form {"CSCA08": someLecture}
        """

        # You can't have sets of sets! Changed this to all lists!
        # Dictionaries are nice
        self._sections = sections
        self._tutorials = tutorials
        self._practicals = practicals
        self._code = code

    def __repr__(self):
        ''' (Course) -> str '''

        return self.getCode() + '{Sections' + str(self.getSections()) \
               + ', Tutorials' + str(self.getTutorials()) + ', Practicals' \
               + str(self.getPracticals()) + '}'
        
    def getSections(self):
        """
        (Course) -> dict of string and set of Lecture
        Return the lecture sections for this Course.
        (Each list within the list is a lecture section.)
        """
        return self._sections
    
    def getTutorials(self):
        """
        (Course) -> set of Tutorial
        Return the tutorial sections for this Course.
        """
        return self._tutorials
    
    def getPracticals(self):
        """
        (Course) -> set of Practical
        Return the practical sections for this Course.
        """
        return self._practicals

    def getCode(self):
        ''' (Course) -> str
        Returns the code for this Course.
        '''

        return self._code
    
    def setSections(self, sections):
        """
        (Course, dict of string and set of Lecture) -> NoneType
        Set the lecture sections for this Course.
        (Each list within the list is a lecture section.)
        """
        self._sections = sections
        
    def setTutorials(self, tutorials):
        """
        (Course, set of Tutorial) -> NoneType
        Set the tutorial sections for this Course.
        """
        self._tutorials = tutorials
        
    def setPracticals(self, practicals):
        """
        (Course, set of Practical) -> NoneType
        Set the practical sections for this Course.
        """
        self._practicals = practicals

    def addSection(self, section):
        ''' (Course, set of Lecture) -> NoneType
        Adds a section to the section list.
        '''

        self._sections[next(iter(section)).getId()] = section

    def addLecture(self, lecture):
        ''' (Course, Lecture) -> NoneType
        Adds a Lecture to the dict of string and set of Lecture (the Section list)
        appropriately. Appropriately refers to adding Lectures in the
        proper Section based on Lecture.getId()
        '''
        #checking if section is already present
        if lecture.getId() in self._sections:
            print("HEY")
            self._sections[lecture.getId()].add(lecture)
        else:
            #creating a new section if needed
            self.addSection({lecture})

    def addTutorial(self, tutorial):
        ''' (Course, Tutorial) -> NoneType
        Adds a Tutorial to this Course.
        '''

        self._tutorials.add(tutorial)

    def addPractical(self, practical):
        ''' (Course, Practical) -> NoneType
        Adds a Practical to this Course.
        '''

        self._practicals.add(practical)