from . courses.course import Course
from . courses.lecture import Lecture
from . courses.tutorial import Tutorial
from . courses.practical import Practical

def blocksToCourses(blocks):
	''' (list of Block) -> list of Course
	Organizes Blocks into newly created Course objects associated by 
	Block.getCourse() as unique ID's.
	'''

	courses = {}

	for block in blocks:
		c = courses[block.getCourse()] if block.getCourse() in \
		        courses else Course([], [], [], block.getCourse())

		{Lecture: c.addLecture, 
		 Tutorial: c.addTutorial, 
		 Practical: c.addPractical}[type(block)](block)

		# add the modified Course back into the dict (you may think this is
		# unnessecary since c is just a reference, but it's for new Course
		# creation.. the Course([], []..) part)
		courses[block.getCourse()] = c

	return courses