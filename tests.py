# test plan

class RegistrationTests(TestCase):
    pass
    # Registration page
    # --------------------------------------------------------------------------
    # Has a form of the correct type
    # Is world-visible
    # We do ~not~ need to test that a registration object is created - that's
    #   django formview
    # We ~do~ need to test that the registration view calls our Stripe function
    #   with correct parameters (but we should mock that out)
    # We ~do~ need to test that the registration view calls:
    #   * moodle_create_user for anyone who doesn't have an associated moodle
    #       user
    #   * moodle_assign_user_to_course for everyone registered, whether or not
    #       they had an existing moodle user
    # Includes course descriptions & instructor images for all upcoming courses


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

