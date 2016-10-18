from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase, Client

from .forms import RegistrationForm

REGULAR_USERNAME = 'user1'
REGULAR_PASSWORD = 'user1_password'

class RegistrationTests(TestCase):
    # Registration page
    # --------------------------------------------------------------------------

    @classmethod
    def setUpClass(cls):
        super(RegistrationTests, cls).setUpClass()
        cls.client = Client()
        cls.regular_user = User.objects.create_user(
            username=REGULAR_USERNAME,
            password=REGULAR_PASSWORD
        )


    # The registration page exists.
    def test_registration_page_url_reverses(self):
        url = reverse('courses:register')
        self.assertEqual(url, '/courses/register/')


    # It has a form of the correct type.
    def test_registration_page_has_form(self):
        url = reverse('courses:register')
        response = self.client.get(url)
        self.assertIn('form', response.context)
        self.assertIsInstance(response.context['form'], RegistrationForm)


    # It is world-visible.
    def test_registration_page_visibility(self):
        # Anonymous users can see it.
        url = reverse('courses:registration')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Logged in users can see it.
        self.client.login(username=REGULAR_USERNAME, password=REGULAR_PASSWORD)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    # It includes course descriptions & instructor images for upcoming courses
    def test_registration_page_course_content(self):
        url = reverse('courses:registration')
        response = self.client.get(url)
        # Create some course objects with varying status
        # Make sure that description and instructor image URL are in page
        # for all upcoming courses
        # Make sure that description and instructor image URL are NOT in page
        # for any past courses
        assert False

    # We do ~not~ need to test that a registration object is created - that's
    # on django formview.

    # Good data tests (it does the right thing when form.is_valid())
    # --------------------------------------------------------------------------

    # The registration view calls our Stripe function with correct parameters
    # on form submit, when the form is valid.
    def test_registration_calls_stripe(self):
        url = reverse('courses:registration')
        response = self.client.post(url)
        # Need to construct post data, import and use mock and add it to the
        # requirements, etc.
        assert False


    def test_registration_calls_moodle_create_user(self):
        url = reverse('courses:registration')
        response = self.client.post(url)
        # Need to construct post data, import and use mock and add it to the
        # requirements, etc.
        # Also need to assert there is no moodle user yet
        assert False


    def test_registration_gets_existing_moodle_user(self):
        url = reverse('courses:registration')
        response = self.client.post(url)
        # Need to construct post data, import and use mock and add it to the
        # requirements, etc.
        # Also need to assert there IS a moodle user
        # And that moodle_create_user is not called in this case
        assert False


    def test_registration_calls_moodle_assign_user(self):
        url = reverse('courses:registration')
        response = self.client.post(url)
        # Need to construct post data, import and use mock and add it to the
        # requirements, etc.
        assert False


    # Bad data tests (it does the right thing when NOT form.is_valid())
    # --------------------------------------------------------------------------

    # The registration view does NOT call our Stripe function on form submit,
    # when the form is invalid.
    def test_invalid_registration_does_not_call_stripe(self):
        assert False


    def test_invalid_registration_does_not_call_moodle_create_user(self):
        assert False


    def test_invalid_registration_does_not_call_moodle_assign_user(self):
        assert False


    # Registration form
    # --------------------------------------------------------------------------
    # Collects name, email, password
    # Autofills name, email, password for people who are logged in
    # Has a checkbox for ALA member, LITA member, neither
    # Has a field of courses available for registration
    # Correctly populates that field from the database



class CourseSetupTests(TestCase):
    pass

    # Course setup page
    # --------------------------------------------------------------------------
    # Has a form of the correct type
    # Is limited to logged-in people with a suitable permission
    # We do ~not~ need to test that a course object is created - that's
    #   django formview
    # We ~do~ need to test that the course setup view calls moodle_create_course
    #   with correct parameters (but we should mock that out)


    # Course setup form
    # --------------------------------------------------------------------------
    # Right now just test that it collects fullname and shortname - this test
    #   will want to be expanded after user feedback



class CourseManagementTests(TestCase):
    pass

    # Course management page
    # --------------------------------------------------------------------------
    # Lists all courses for which you have registered
    #   decreasing by date
    #   clearly indicating current vs past
    #   includes link to moodle course pages
    # Has a deemphasized cancel registration option for courses which have not
    #   yet started
    # Has an emphasized button to register for future courses
    # Includes an instructor image
    # Restricted to logged-in users
    # You can only see your registrations, not anyone else's

    # Course withdrawal page
    # --------------------------------------------------------------------------
    # Accessible only to logged-in users
    # You can only withdraw yourself
    #   ...unless you have special permissions
    # Sets a withdrawn status on your registration
    # Calls a moodle_remove_user_from_course function



# Open questions
# --------------------------------------------------------------------------
# What fields does our course object need?
# How do we tell if people already have an associated Moodle user?
# What information must the registration form collect (or autofill) to create
#   moodle users?
