''' Scrape Test '''

import optipeach

# get all CSC Courses
b = optipeach.UTSCScraper.pullAllBlocks(['CSC'])
s = optipeach.blocksToCourses(b)
print(s)