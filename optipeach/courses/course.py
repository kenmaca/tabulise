class Course():
    def __init__(self, sections, tutorials, practicals, code):
        """
        (Course, list of list of Lecture, list of Tutorial, list of Practical, 
        str) -> Course
        """

        # You can't have sets of sets! Changed this to all lists!
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
        (Course) -> list of list of Lecture
        Return the lecture sections for this Course.
        (Each list within the list is a lecture section.)
        """
        return self._sections
    
    def getTutorials(self):
        """
        (Course) -> list of Tutorial
        Return the tutorial sections for this Course.
        """
        return self._tutorials
    
    def getPracticals(self):
        """
        (Course) -> list of Practical
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
        (Course, list of list of Lecture) -> NoneType
        Set the lecture sections for this Course.
        (Each list within the list is a lecture section.)
        """
        self._sections = sections
        
    def setTutorials(self, tutorials):
        """
        (Course, list of Tutorial) -> NoneType
        Set the tutorial sections for this Course.
        """
        self._tutorials = tutorials
        
    def setPracticals(self, practicals):
        """
        (Course, list of Practical) -> NoneType
        Set the practical sections for this Course.
        """
        self._practicals = practicals

    def addSection(self, section):
        ''' (Course, list of list of Lecture) -> NoneType
        Adds a section to the section list.
        '''

        self._sections.append(section)

    def addLecture(self, lecture):
        ''' (Course, Lecture) -> NoneType
        Adds a Lecture to the list of list of Lecture (the Section list)
        appropriately. Appropriately refers to adding Lectures in the
        proper Section based on Lecture.getId()
        '''

        for section in self._sections:
            
            # assumes that integrity of the section list is solid, so
            # all we need to check is the first Lecture in this section
            if section[0].getId() == lecture.getId():
                section.append(lecture)
                return

        # section doesn't exist, so make it
        self.addSection([lecture])

    def addTutorial(self, tutorial):
        ''' (Course, Tutorial) -> NoneType
        Adds a Tutorial to this Course.
        '''

        self._tutorials.append(tutorial)

    def addPractical(self, practical):
        ''' (Course, Practical) -> NoneType
        Adds a Practical to this Course.
        '''

        self._practicals.append(practical)