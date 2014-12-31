import sys
import os

# add local packages to Python path
path = os.path.abspath(os.path.dirname(__file__))
for subdir in ["/.."]:
    if not (path + subdir) in sys.path:
        sys.path.insert(0, os.path.abspath(path + subdir))
del subdir

import exceptions
