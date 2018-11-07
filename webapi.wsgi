activate_this = '/home/chenyu_shi/venv/bin/activate_this.py'

with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from webapi import app as application
