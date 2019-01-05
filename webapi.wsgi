# activate Python virtual environment
# PlEASE IGNORE THIS LINE 1
import sys
activate_this = '/home/chenyu_shi/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

if sys.version_info[0]<3:       # require python3
    raise Exception("Python3 required! Current (wrong) version: '%s'" % sys.version_info)

# insert directory to system path
sys.path.insert(0,"home/chenyu_shi/SpeciesLookup")
from webapi import app as application

