import sys
activate_this = '/home/pi/Desktop/env/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(),dict(__file__=activate_this))

if sys.version_info[0]<3:       # require python3
    raise Exception("Python3 required! Current (wrong) version: '%s'" % sys.version_info)

sys.path.insert(0,'/home/pi/Desktop/SpeciesLookup')
from webapi import app as application
