# Documentation

* how to set up and configure the moodle instance
    * including web services (https://docs.moodle.org/31/en/Using_web_services)
        * turn on web services
        * enable REST api
    * and security
* server dependencies

## Enable and configure web services

While logged in to your Moodle instance as an administrator:
* Enable web services
    * Access `Administration > Site administration > Advanced` features
    * Check 'Enable web services' then click 'Save Changes'
    * Access `Administration > Site administration > Plugins > Web services > Manage protocols`
    * Enable the REST protocol and save changes
* Create a custom service
    * Access `Administration > Site administration > Plugins > Web services > External services`
    * Add a custom service
    * It can have any name
    * Click `Enabled`
    * Click `Authorised users only`
    * Save it
    * Now you can add functions to it; add the `core_course_create_courses` function
* Create a web services user
    * Access `Administration > Site administration > Users > Accounts > Add a new user`
* Create a web services role
    * Access `Administration > Site administration > Users > Permissions > Define roles`
    * Must be assignable in the System scope
    * Must have the following capabilities: `moodle/webservice:createtoken`, `webservice/rest:use`, `moodle/course:create`, `moodle/course:visibility`
* Assign your new role to your new user (`Administration > Site administration > Users > Permissions > Assign system roles`)
* Authorise your user
    * Under `Administration > Site administration > Plugins > Web services > External services`, `Authorised users` should be an option for your new web service
    * Add your web service user
