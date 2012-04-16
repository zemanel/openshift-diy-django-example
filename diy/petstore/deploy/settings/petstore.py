""""""
import os

BROKER_URL = os.environ['OPENSHIFT_NOSQL_DB_URL']

TIME_ZONE = 'UTC'

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
