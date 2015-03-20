from . scraper import Scraper
from .. courses.lecture import Lecture
from .. courses.tutorial import Tutorial
from .. courses.practical import Practical
from .. courses.timeslot import TimeSlot
import json

URL_BASE = 'http://coursefinder.utoronto.ca/course-search/search'
URL_ALL = '%s/courseSearch/course/search' % URL_BASE
CAMPUSES = 'St. George,Scarborough,Mississauga'

class UofTScraper(Scraper):
	''' A scraper used to pull all courses from the UofT Course Finder website
	found at http://coursefinder.utoronto.ca.
	'''

	@staticmethod
	def pullAllBlocks(campus = CAMPUSES):
		''' (str) -> list of Block
		Grabs all available Blocks from the Course Finder website in the
		specified campus(es).

		REQ: campus contains one or more of the following: St. George,
		Scarborough, Mississauga separated by commas (with no trailing spaces).
		'''

		return Scraper.pullRaw(URL_ALL, {'queryText' : '', 'requirements' : '', 'campusParam' : campus}).json()['aaData']