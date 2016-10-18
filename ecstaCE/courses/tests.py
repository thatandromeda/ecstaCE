from datetime import date, timedelta
from tempfile import NamedTemporaryFile

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase, Client

from .forms import RegistrationForm
from .models import Course, Instructor

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
        url = reverse('courses:register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Logged in users can see it.
        self.client.login(username=REGULAR_USERNAME, password=REGULAR_PASSWORD)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    # It includes course descriptions & instructor images for upcoming courses
    def test_registration_page_course_content(self):
        # Set up courses.
        # This course has not yet started, and should appear on the page.
        image_future = NamedTemporaryFile(suffix=".jpg").name
        instructor_future = Instructor(
            name='Carla Hayden',
            institution='Library of Congress',
            picture=image_future
        )
        instructor_future.save()

        description_future = 'Had Henriette Avram only known it all would be different'

        course_future = Course(
            full_name='Introduction to SQL for Librarians',
            short_name='SQL2016',
            description=description_future,
            start_date=date.today() + timedelta(days=1),
            end_date=date.today() + timedelta(days=8)
        )
        course_future.save()
        course_future.instructors.add(instructor_future)

        # This course is in progress, and should not appear.
        image_current = NamedTemporaryFile(suffix=".jpg").name
        instructor_current = Instructor(
            name='Judith Krug',
            institution='American Library Association',
            picture=image_current
        )
        instructor_current.save()

        description_current = 'Meow'

        course_current = Course(
            full_name='Web Programming with Cat GIFs',
            short_name='GIF2016',
            description=description_current,
            start_date=date.today() - timedelta(days=1),
            end_date=date.today() + timedelta(days=6)
        )
        course_current.save()
        course_current.instructors.add(instructor_current)

        # This course is over, and should not appear.
        image_past = NamedTemporaryFile(suffix=".jpg").name
        instructor_past = Instructor(
            name='Zoia Horn',
            institution='Bucknell University',
            picture=image_past
        )
        instructor_past.save()

        description_past = 'See enclosing codebase'

        course_past = Course(
            full_name='Hacking Legacy Infrastructure for Fun',
            short_name='META',
            description=description_past,
            start_date=date.today() - timedelta(days=8),
            end_date=date.today() - timedelta(days=1)
        )
        course_past.save()
        course_past.instructors.add(instructor_past)

        url = reverse('courses:register')
        response = self.client.get(url)
        # Make sure that description and instructor image URL are in page
        # for all upcoming courses
        self.assertContains(response, description_future)
        self.assertContains(response, url_future)

        # Make sure that description and instructor image URL are NOT in page
        # for any past courses
        self.assertNotContains(response, description_current)
        self.assertContains(response, url_current)
        self.assertNotContains(response, description_past)
        self.assertContains(response, url_past)

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
