"""
Default settings for local development, with defaults for Sqlite database
and local media and static files storage
"""

from petstore.settings import *
from unipath import FSPath as Path

DEBUG = True
TEMPLATE_DEBUG = DEBUG

#print PROJECT_DIR

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': PROJECT_DIR.child('var').child('petstore.sqlite'),
    }
}

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = PROJECT_DIR.child('var').child('media')

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = PROJECT_DIR.child('var').child('static')

