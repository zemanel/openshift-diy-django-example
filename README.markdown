About
======
A Django 1.4 example project for deployment on "Do It Yourself" application type of http://openshift.redhat.com 

Example deployment: http://petstore-zemanel.rhcloud.com

Notes
=====

* On every deployment, the 'deploy' hook script performs the following actions:
  * [re-]creates a python virtual environment on $OPENSHIFT_DATA_DIR/$OPENSHIFT_APP_NAME and activates it
  * installs a pip requirements file named 'requirements.txt' which is located on the root of the repo
  * runs the 'syncdb', 'migrate' and 'collectstatic' django commands
* re-creating the python virtual environment makes deployments slower but keeps things tight. Pip downloads are cached on the '${OPENSHIFT_TMP_DIR}.pip/cache' folder
* the 'start' hook script runs gunicorn as a daemon, binded on $OPENSHIFT_INTERNAL_IP:$OPENSHIFT_INTERNAL_PORT, with a pid file written to '${OPENSHIFT_DATA_DIR}gunicorn.pid', which is then used by the 'stop' hook to terminate the gunicorn process
* there are separated stdout and access logs, outputted to $OPENSHIFT_LOG_DIR  
    


