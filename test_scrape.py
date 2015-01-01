''' Scrape Test '''

import optipeach

# get all Courses
b = optipeach.UTSCScraper.pullBlocks('', '')
s = optipeach.blocksToCourses(b)
print(s)