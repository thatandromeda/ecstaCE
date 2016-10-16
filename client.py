# connect to Moodle instance
import requests

MOODLE_BASE_URL = 'http://localhost/~ayelton/moodle'
MOODLE_API_ENDPOINT = '/webservice/rest/server.php'
MOODLE_AUTH_TOKEN = ''
MOODLE_COURSE_CREATE = 'core_course_create_courses'

url = '{domain}{endpoint}'.format(
    domain=MOODLE_BASE_URL, endpoint=MOODLE_API_ENDPOINT)
payload = {'wstoken': MOODLE_AUTH_TOKEN, 'wsfunction': MOODLE_COURSE_CREATE}
response = requests.get(url, params=payload)
print response
print response.content
