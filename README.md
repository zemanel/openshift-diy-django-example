About
=====

A Django 1.4.5 example project for deployment on "Do It Yourself" application type of http://openshift.redhat.com

Example deployment: http://petstore-zemanel.rhcloud.com

Setting up Openshift
--------------------

Create the Openshift application with a DIY and Postgresql 8.4 cartridge

    $ rhc app create djangoexample diy-0.1 postgresql-8.4 --from-code https://github.com/zemanel/openshift-diy-django-example.git

The app should be working out-of-the-box on *http://djangoexampletest-<YOUR NAMESPACE>.rhcloud.com*

Pre deploy stage
----------------

On every deployment, the 'deploy' hook script performs the following actions:

* [re-]creates a python virtual environment on $OPENSHIFT_DATA_DIR/venv and activates it
* installs a pip requirements file named 'requirements.txt' which is located on the root of the repo.
The virtualenv is versioned based on the requirements.txt MD5, to speed up deployments
* runs the 'syncdb', 'migrate' and 'collectstatic' django commands
* Pip downloads are cached on the '${OPENSHIFT_TMP_DIR}.pip/cache' folder
* the 'start' hook script runs gunicorn as a daemon, binded on $OPENSHIFT_INTERNAL_IP:$OPENSHIFT_INTERNAL_PORT,
with a pid file written to '${OPENSHIFT_DATA_DIR}gunicorn.pid', which is then used by the 'stop' hook to terminate the gunicorn process
* there are separated stdout and access logs, outputted to $OPENSHIFT_LOG_DIR  
    

Developing locally
------------------

A *settings_localdev.py* module has *out of the box* defaults for using local folders and an Sqlite database.

It can easily be used this way:

    $ export DJANGO_SETTINGS_MODULE=settings_localdev

    $ dj syncdb

    $ dj migrate

The *settings_localdev.py* module approach can be duplicated into another module not checked into source control and
further customized, for example.

Contributing
------------

git-flow (https://github.com/nvie/gitflow) is used in the devevelopment process.

To contribute, submit pull requests to the 'develop' branch or a feature branch, which will be tested and then merged.







