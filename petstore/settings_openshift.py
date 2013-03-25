# -*- coding: utf-8 -*-
"""
Openshift specific Django settings override
"""
import os
from petstore.settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE'    : 'django.db.backends.postgresql_psycopg2',
        'NAME'      : os.environ['OPENSHIFT_APP_NAME'],
        'USER'      : os.environ['OPENSHIFT_DB_USERNAME'],
        'PASSWORD'  : os.environ['OPENSHIFT_DB_PASSWORD'],
        'HOST'      : os.environ['OPENSHIFT_DB_HOST'],
        'PORT'      : os.environ['OPENSHIFT_DB_PORT'],
        }
}

# add your own custom settings here

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    os.environ['OPENSHIFT_GEAR_DNS']
]
