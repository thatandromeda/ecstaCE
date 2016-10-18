# connect to Moodle instance
import requests

from credentials import MOODLE_AUTH_TOKEN

MOODLE_BASE_URL = 'http://localhost/~ayelton/moodle'
MOODLE_API_ENDPOINT = '/webservice/rest/server.php'
MOODLE_COURSE_CREATE = 'core_course_create_courses'

MOODLE_URL = '{domain}{endpoint}'.format(
        domain=MOODLE_BASE_URL, endpoint=MOODLE_API_ENDPOINT)


# See https://github.com/moodle/moodle/blob/f73f93846940168fc79ee83036e977a0b3cfcbef/course/externallib.php
# for available course parameters
# See also https://github.com/squidsoup/muddle.py/blob/master/muddle/api.py,
# which sadly seems to be no longer pip installable.

def create_course(fullname, shortname, categoryid=1):
    payload = {'wstoken': MOODLE_AUTH_TOKEN,
               'wsfunction': MOODLE_COURSE_CREATE,
               'moodlewsrestformat': 'json',
              'courses[0][fullname]': fullname,
              'courses[0][shortname]': shortname,
              'courses[0][categoryid]': categoryid}
    # Should return something like [{"id":2,"shortname":"test"}]

    response = requests.get(MOODLE_URL, params=payload)
